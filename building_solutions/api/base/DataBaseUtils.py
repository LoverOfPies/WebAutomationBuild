from typing import List

from peewee import Model, ForeignKeyField, DoubleField, IntegerField, BooleanField, DateField, CharField

from api.base import FilterUtils, AutocompleteUtils
from api.base.Cache import Cache
from api.base.MyAppException import MyAppException

cache = Cache()

ERROR_METH = 'error'
INSERT_METH = 'insert'
GET_METH = 'get'


def get_model(name: str) -> Model:
    """
    Return table object from cache

    :param: name (str): table name

    :return: table object
    """
    return cache.get_model_by_name(name)


def get_record(model, values):
    """
    Return record object by filter

    :param model: table object
    :param values: field values for building the filter

    :return: record object
    """
    condition = FilterUtils.get_equals_filter(model, values)
    if condition is None:
        return None
    try:
        obj = model.get(condition)
    except model.DoesNotExist:
        obj = None
    return obj


def get_records(model, values=None) -> List:
    """
    Return records object by filter

    :param model: table object
    :param values: field values for building the filter

    :return: records object
    """
    condition = FilterUtils.get_equals_filter(model, values)
    if condition is None:
        return [row for row in model.select()]
    return [row for row in model.select().where(condition)]


def update_record(collection, id_row, data):
    model = get_model(collection)
    row = model.get_or_none(id=id_row)
    field = data['field']
    value = data['value']
    versioning_model = get_model('versioning')
    if isinstance(row, versioning_model):
        AutocompleteUtils.create_new_version(model, row, data)
        return True
    field_data = dict(row.__data__)
    field_data[field] = value
    query = model.update(**field_data).where(model.id == row.id)
    if query.execute() == 0:
        return False
    return True


def insert_record(model, values):
    with model._meta.database.atomic() as transaction:
        try:
            obj = model.insert(values).execute()
            transaction.commit()
        except Exception as e:
            transaction.rollback()
            obj = None
    return obj


def delete_record(model, row):
    # check delete row for constraints
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


def get_or_insert(model, values):
    meth = ERROR_METH
    obj = get_record(model, values)
    if obj:
        meth = GET_METH
    else:
        obj = insert_record(model, values)
        if obj:
            meth = INSERT_METH
    return obj, meth


def get_field_type(field_object):
    """
    Метод для получения типа поля
    """
    field_type = None
    if isinstance(field_object, CharField):
        field_type = "text"
    if isinstance(field_object, ForeignKeyField):
        field_type = "selectable"
    if isinstance(field_object, DoubleField):
        field_type = "float"
    if isinstance(field_object, IntegerField):
        field_type = "integer"
    if isinstance(field_object, BooleanField):
        field_type = "boolean"
    if isinstance(field_object, DateField):
        field_type = "date"
    if not field_type:
        raise MyAppException(f'Не определён тип данных для поля {field_object}')
    return field_type
