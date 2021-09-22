import sys

models_paths = {
    'base_unit': 'src.db.models.base.BaseUnit.BaseUnit',
    'prop': 'src.db.models.base.Prop.Prop',
    'unit': 'src.db.models.base.Unit.Unit',

    'material': 'src.db.models.material.Material.Material',
    'material_category': 'src.db.models.material.MaterialCategory.MaterialCategory',
    'material_group': 'src.db.models.material.MaterialGroup.MaterialGroup',
    'material_subgroup': 'src.db.models.material.MaterialSubgroup.MaterialSubgroup',

    'base_volume': 'src.db.models.project.BaseVolume.BaseVolume',
    'equipment': 'src.db.models.project.Equipment.Equipment',
    'estimate': 'src.db.models.project.Estimate.Estimate',
    'project': 'src.db.models.project.Project.Project',

    'city': 'src.db.models.provider.City.City',
    'product': 'src.db.models.provider.Product.Product',
    'provider': 'src.db.models.provider.Provider.Provider',

    'work': 'src.db.models.work.Work.Work',
    'work_group': 'src.db.models.work.WorkGroup.WorkGroup',
    'work_material': 'src.db.models.work.WorkMaterial.WorkMaterial',
    'work_stage': 'src.db.models.work.WorkStage.WorkStage',
    'work_technology': 'src.db.models.work.WorkTechnology.WorkTechnology'
}


sidebar = [
    {
        "title": "Базовые единицы",
        "icon": "box",
        "name": "base_unit"
    },
    {
        "title": "Свойства",
        "icon": "box",
        "name": "prop"
    },
    {
        "title": "Единицы измерения",
        "icon": "box",
        "name": "unit"
    },
    {
        "title": "Поставщики",
        "icon": "box",
        "name": "provider"
    },
    {
        "title": "Материалы",
        "icon": "box",
        "name": "material"
    },
    {
        "title": "Работы",
        "icon": "box",
        "name": "work"
    },
    {
        "title": "Проекты",
        "icon": "box",
        "name": "project"
    }
]


def get_model_by_name(name):
    model_path = models_paths.get(name)
    if model_path is None:
        return model_path
    return load_class(model_path)


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)


def add_row(collection, data):

    return False


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
