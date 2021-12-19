import configparser
import json

from app import db
from src import FilterUtils
from src.Cache import Cache

cache = Cache()


def get_model(name):
    """
    Return table object from cache

    :param name: table name

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


def insert_record(model, values):
    with db.database.atomic() as transaction:
        try:
            obj = model.insert(values).execute()
            transaction.commit()
        except:
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
    meth = "error"
    obj = get_record(model, values)
    if obj:
        meth = "get"
    else:
        obj = insert_record(model, values)
        if obj:
            meth = "insert"
    return obj, meth


def check_data(data, model):
    for field in data.keys():
        if not hasattr(model, field):
            return False
    return True


# TODO: Rewrite this
def init_base():
    config = configparser.ConfigParser()
    config.read('first.ini')
    if config['BASE']['first_init'] == 'False':
        return
    config['BASE']['first_init'] = 'False'
    with open('first.ini', 'w') as configfile:
        config.write(configfile)
    table_info_model = cache.get_table_info_model()
    table_info_model.create_table()
    filter_info_model = cache.get_filter_info_model()
    filter_info_model.create_table()
    action_info_model = cache.get_action_info_model()
    action_info_model.create_table()
    with open('table_info.json', 'r', encoding='utf-8') as f:
        encode_json = json.load(f)
    data_models_data = encode_json['models_info']
    for value in data_models_data:
        get_or_insert(table_info_model, value)
    data_filter_data = encode_json['filters_info']
    for value in data_filter_data:
        value["table"] = table_info_model.select().where(table_info_model.name == value["table"]).get()
        get_or_insert(filter_info_model, value)
    data_action_data = encode_json['actions_info']
    for value in data_action_data:
        value["table"] = table_info_model.select().where(table_info_model.name == value["table"]).get()
        get_or_insert(action_info_model, value)
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