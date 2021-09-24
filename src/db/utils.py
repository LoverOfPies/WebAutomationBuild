import json

from app import db
from src.Cache import Cache

cache = Cache()


def get_model(name):
    return cache.get_model_by_name(name)


def add_row(collection, data):
    model = cache.get_model_by_name(collection)
    if model is None:
        return False
    decoded_data = json.loads(data)
    if check_data(decoded_data, model):
        model.insert(decoded_data).execute()
    return True


def delete_row(collection, id_row):
    model = cache.get_model_by_name(collection)
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
    model = cache.get_model_by_name(collection)
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
    for table_name in cache.get_sidebar_fields():
        table_info = cache.get_table_info(table_name)
        data.append({"title": table_info.title, "icon": table_info.icon, "name": table_info.name})
    return data


def init_base():
    # Проверка на first_init
    table_info_model = cache.get_table_info_model()
    table_info_model.create_table()
    with open('table_info.json', 'r', encoding='utf-8') as f:
        data = json.load(f)['models_info']
        for value in data:
            with db.database.atomic() as transaction:  # Opens new transaction.
                try:
                    table_info_model.insert(value).execute()
                except:
                    transaction.rollback()
                    continue
    table_info_all = (table_info_model.select())
    for table_info in table_info_all:
        table_model = get_model(table_info.name)
        create_table_with_backref(table_model)


def create_table_with_backref(model):
    backref_tables = model._meta.model_backrefs
    for ref in model._meta.refs:
        if not ref.rel_model.table_exists():
            create_table_with_backref(ref.rel_model)
    model.create_table()
    for backref_table in backref_tables:
        create_table_with_backref(backref_table)
