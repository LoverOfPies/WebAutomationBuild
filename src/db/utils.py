import json
import sys

# 'table_name': (path, icon, table_name (Понятное человеку)),
models_info = {
    'base_unit': ('src.db.models.base.BaseUnit.BaseUnit', 'box', 'Базовые единицы'),
    'prop': ('src.db.models.base.Prop.Prop', 'box', 'Свойства'),
    'unit': ('src.db.models.base.Unit.Unit', 'box', 'Единицы измерения'),

    'material': ('src.db.models.material.Material.Material', 'box', 'Материалы'),
    'material_category': ('src.db.models.material.MaterialCategory.MaterialCategory', 'box', 'Категории материалов'),
    'material_group': ('src.db.models.material.MaterialGroup.MaterialGroup', 'box', 'Группы материалов'),
    'material_subgroup': ('src.db.models.material.MaterialSubgroup.MaterialSubgroup', 'box', 'Подгруппы материалов'),

    'base_volume': ('src.db.models.project.BaseVolume.BaseVolume', 'box', 'Базовый объём'),
    'equipment': ('src.db.models.project.Equipment.Equipment', 'box', 'Комплектации'),
    'estimate': ('src.db.models.project.Estimate.Estimate', 'box', 'Расчёты'),
    'project': ('src.db.models.project.Project.Project', 'box', 'Проекты'),

    'city': ('src.db.models.provider.City.City', 'box', 'Города'),
    'product': ('src.db.models.provider.Product.Product', 'box', 'Товары'),
    'provider': ('src.db.models.provider.Provider.Provider', 'box', 'Поставщики'),

    'work': ('src.db.models.work.Work.Work', 'box', 'Работы'),
    'work_group': ('src.db.models.work.WorkGroup.WorkGroup', 'box', 'Группы работ'),
    'work_material': ('src.db.models.work.WorkMaterial.WorkMaterial', 'box', 'Материалы для работы'),
    'work_stage': ('src.db.models.work.WorkStage.WorkStage', 'box', 'Стадии работ'),
    'work_technology': ('src.db.models.work.WorkTechnology.WorkTechnology', 'box', 'Технологии работ')
}

sidebar_fields = ("base_unit", "prop", "unit", "provider", "material", "work", "project")


def get_model_by_name(name):
    model_path, _, _ = models_info.get(name)
    if model_path is None:
        return model_path
    return load_class(model_path)


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)


def add_row(collection, data):
    model = get_model_by_name(collection)
    if model is None:
        return False
    decoded_data = json.loads(data)
    if check_data(decoded_data, model):
        model.insert(decoded_data).execute()
    return True


def delete_row(collection, id_row):
    model = get_model_by_name(collection)
    if model is None:
        return False
    row = model.get_or_none(id=id_row)
    if row is None:
        return False
    foreign_tables = [table for table in row._meta.model_backrefs]
    for foreign_table in foreign_tables:
        foreign_keys = [key for key in foreign_table._meta.refs]
        for foreign_key in foreign_keys:
            if foreign_key.rel_model == model:
                link_quantity = len(foreign_table.select().where(foreign_key == row))
                if link_quantity > 0:
                    return False
    row.delete_instance()
    return True


def update_row(collection, id_row, data):
    model = get_model_by_name(collection)
    if model is None:
        return False
    row = model.get_or_none(id=id_row)
    if row is None:
        return False
    field = data['field']
    if field is None:
        return False
    value = data['value']
    if value is None:
        return False
    field_data = dict(row.__data__)
    field_data[field] = value
    query = model.update(**field_data).where(model.id == row.id)
    if query.execute() == 0:
        return False
    return True


def check_data(data, model):
    for field in data.keys():
        if not hasattr(model, field):
            return False
    return True


def create_sidebar():
    data = []
    for table_name in sidebar_fields:
        _, icon, title = models_info.get(table_name)
        data.append({"title": title, "icon": icon, "name": table_name})
    return data
