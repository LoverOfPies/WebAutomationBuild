import configparser
import json
import ast

from peewee import ForeignKeyField, DoubleField, IntegerField, BooleanField, DateField

from app import db
from src.Cache import Cache

cache = Cache()


def get_model(name):
    return cache.get_model_by_name(name)


def get_row(model, values):
    condition = get_condition(model, values)
    if condition is None:
        return None
    try:
        obj = model.get(condition)
    except model.DoesNotExist:
        obj = None
    return obj


def insert_row(model, values):
    with db.database.atomic() as transaction:
        try:
            obj = model.insert(values).execute()
            transaction.commit()
        except:
            transaction.rollback()
            obj = None
    return obj


def get_or_insert(model, values):
    meth = "error"
    obj = get_row(model, values)
    if obj:
        meth = "get"
    else:
        obj = insert_row(model, values)
        if obj:
            meth = "insert"
    return obj, meth


def check_data(data, model):
    for field in data.keys():
        if not hasattr(model, field):
            return False
    return True


def get_condition(model, values):
    filters = []
    for value in values:
        if hasattr(model, value):
            filter_field = getattr(model, value)
            filter_value = values[value]
            filters.append(filter_field == filter_value)
    condition = None
    for i in range(len(values)):
        if i == 0:
            condition = filters[i]
            continue
        condition = condition & filters[i]
    return condition


def add_row(collection, data):
    model = get_model(collection)
    if model is None:
        return None
    decoded_data = ast.literal_eval(str(data))
    if not check_data(decoded_data, model):
        return None
    obj, meth = get_or_insert(model, data)
    if meth == "get":
        return None
    res = model.select().where(model.id == obj)
    return res


def delete_row(collection, id_row):
    model = get_model(collection)
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
    model = get_model(collection)
    if model is None:
        return False
    if 'params' not in data.keys():
        return False
    data = data['params']
    if 'mode' in data.keys():
        if data['mode'] == 'many_to_many':
            parent = data['parent']
            parent_id = data['parent_id']
            child = data['child']
            child_id = id_row
            checked = data['value']
            values = {parent: parent_id, child: child_id}
            if checked:
                insert_row(model, values)
            else:
                obj = get_row(model, values)
                obj.delete_instance()
            return True
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


def get_filter_data(model, values):
    keys = list(values.keys())
    if "mode" in keys:
        keys.remove("mode")
    for i in (range(len(keys))):
        if i + 1 == len(keys):
            inner_model_name = keys[i]
            data = [res for res in model.select().where(getattr(model, inner_model_name) == values[inner_model_name]).dicts()]
            return data
        if values[keys[i + 1]] == "":
            inner_model_name = keys[i + 1]
            inner_model = get_model(inner_model_name)
            inner_ids = [id for id in inner_model.select(getattr(inner_model, "id")).where(getattr(inner_model, keys[i]) == values[keys[i]])]
            data = recursive_filter(inner_model_name, keys[i+1:], inner_ids, model)
            return data


def recursive_filter(model_name, keys, obj_ids, parent_model):
    data = []
    for i in (range(len(keys))):
        if i + 1 == len(keys):
            for obj_id in obj_ids:
                data = data + [res for res in parent_model.select().where(getattr(parent_model, model_name) == obj_id).dicts()]
            return data
        inner_model_name = keys[i + 1]
        inner_model = get_model(inner_model_name)
        inner_ids = []
        for obj_id in obj_ids:
            inner_ids = inner_ids + [res for res in inner_model.select(getattr(inner_model, "id")).where(getattr(inner_model, keys[i]) == obj_id)]
        data = recursive_filter(inner_model_name, keys[i+1:], inner_ids, parent_model)
        return data


def get_many_data(model, values):
    data = None
    del values['mode']
    child_name = values['child']
    del values['child']
    child_all_data = None
    if hasattr(model, child_name):
        child_model = getattr(model, child_name).rel_model
        child_all_data = [row for row in child_model.select().dicts()]
    condition = get_condition(model, values)
    select_ids = []
    if condition:
        child_select_data = [row for row in model.select(getattr(model, child_name)).where(condition).dicts()]
        select_ids = [row_value[child_name] for row_value in child_select_data]
    if child_all_data:
        data = []
        for child_data in child_all_data:
            if child_data['id'] in select_ids:
                child_data['checked'] = True
            else:
                child_data['checked'] = False
            data.append(child_data)
    return data


def create_sidebar():
    data = []
    for table_name in cache.get_sidebar_fields():
        table_info = cache.get_table_info(table_name).get()
        data.append({"title": table_info.title, "icon": table_info.icon, "name": table_info.name})
    return data


def get_dicts_info():
    all_table_info = cache.get_table_info_model().select()
    data = []
    for table_info in all_table_info:
        value = {"name": table_info.name, "title": table_info.title}
        data.append(value)
    return data


def get_dict_info(collection, params):
    table_info = cache.get_table_info(collection).get()
    data = {"title": table_info.title}

    fields = []
    model = get_model(collection)
    if table_info.many_to_many:
        data['mode'] = 'many_to_many'
    for field_name in model._meta.fields:
        if field_name in ('id', 'uuid', 'version_number'):
            continue
        if table_info.many_to_many:
            if params and 'parent' in params.keys():
                if field_name != params['parent']:
                    value = getattr(model, field_name)
                    fields.append({"key": "name", "label": value.verbose_name})
                    data['child'] = field_name
                continue
        value = getattr(model, field_name)
        field_info = {"key": field_name, "label": value.verbose_name}
        if field_name == 'name':
            field_info["sortable"] = True
        if isinstance(value, ForeignKeyField):
            field_info["type"] = "selectable"
        if isinstance(value, DoubleField):
            field_info["type"] = "float"
        if isinstance(value, IntegerField):
            field_info["type"] = "integer"
        if isinstance(value, BooleanField):
            field_info["type"] = "boolean"
        if isinstance(value, DateField):
            field_info["type"] = "date"
        fields.append(field_info)
    data["fields"] = fields

    filters = []
    filter_info_model = cache.get_filter_info_model()
    filters_info = filter_info_model.select().where(filter_info_model.table == table_info)\
        .order_by(filter_info_model.id.asc())
    for filter_info in filters_info:
        filters.append({"key": filter_info.key, "label": filter_info.label, "multiple": filter_info.multiple})
    data["filters"] = filters

    actions = []
    action_info_model = cache.get_action_info_model()
    actions_info = action_info_model.select().where(action_info_model.table == table_info)
    for action_info in actions_info:
        actions.append({"action": action_info.action, "label": action_info.label, "to": action_info.to})
    data["actions"] = actions

    return data


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
