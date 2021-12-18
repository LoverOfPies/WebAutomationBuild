import configparser
import json

from peewee import ForeignKeyField, DoubleField, IntegerField, BooleanField, DateField

from app import db
from src.Cache import Cache

cache = Cache()


def get_model(name):
    """
    Return table object from cache

    :param name: table name

    :return: table object
    """
    return cache.get_model_by_name(name)


def get_row(model, values):
    """
    Return record object by filter

    :param model: table object
    :param values: field values for building the filter

    :return: record object
    """
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
    """
    Return equals filter by fields and values
    format: {"field": value, ...}

    :param model: table object
    :param values: fields and values for filter

    :return: filter
    """
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
    """
    Add record in table

    :param collection: table name
    :param data: fields and values

    :return: new record or None
    """
    model = get_model(collection)
    if model is None:
        return None
    if not check_data(data, model):
        return None
    obj, meth = get_or_insert(model, data)
    if meth == "get":
        return None
    row_object = model.select().where(model.id == obj)
    return row_object


def delete_row(collection, id_row) -> bool:
    """
    Delete record from a table by id

    :param collection: table name
    :param id_row: record id

    :return: bool
    """
    model = get_model(collection)
    if model is None:
        return False
    row = model.get_or_none(id=id_row)
    if row is None:
        return False
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


def update_row(collection, id_row, data) -> bool:
    """
    Update record field by id

    :param collection: table name
    :param id_row: record id
    :param data: dict with request parameters

    :return: bool
    """
    model = get_model(collection)
    if model is None:
        return False

    if 'mode' in data.keys():
        if data['mode'] == 'many_to_many':
            parent = data['parent']
            parent_id = data['parent_id']
            child = data['child']
            # radiobutton change
            # current = -1 - remove flag
            # prev = -1 - first init
            if 'prev' in data.keys():
                prev = data['prev']
                current = data['current']
                if prev != -1:
                    values = {parent: parent_id, child: prev}
                    obj = get_row(model, values)
                    obj.delete_instance()
                if current != -1:
                    values = {parent: parent_id, child: current}
                    insert_row(model, values)
            # classic many_to_many
            # add or remove record when switching checkbox
            else:
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


def get_filter_data(model, values) -> list:
    """
    Return records from table

    :param model: table object
    :param values: dict
    {
        'field': 'value',
        ...
    }

    :return: data
    """
    keys = list(values.keys())
    for i, model_name in enumerate(keys):
        # simple filter with one element in grid
        if 1 == len(keys):
            data = [res for res in
                    model.select().where(getattr(model, model_name) == values[model_name]).dicts()]
            return data
        # advance filter with many element in grid
        # start filter from first table in chain
        if values[keys[i + 1]] == "":
            inner_model_name = keys[i + 1]
            inner_model = get_model(inner_model_name)
            inner_ids = [inner_id for inner_id in inner_model.select(getattr(inner_model, "id")).where(
                getattr(inner_model, model_name) == values[model_name])]
            data = recursive_filter(inner_model_name, keys[i + 1:], inner_ids, model)
            return data


def recursive_filter(model_name, keys, obj_ids, parent_model) -> list:
    """
    Return records from chain filter

    :param model_name: current table name in chain
    :param keys: other chain params
    :param obj_ids: ids for filter current table
    :param parent_model: original table object

    :return: data
    """
    data = []
    for i, val in enumerate(keys):
        # find last table in chain
        # get data from original table with ids constraints
        if i + 1 == len(keys):
            for obj_id in obj_ids:
                data = data + [res for res in
                               parent_model.select().where(getattr(parent_model, model_name) == obj_id).dicts()]
            return data
        # get ids from next table in chain
        inner_model_name = keys[i + 1]
        inner_model = get_model(inner_model_name)
        inner_ids = []
        for obj_id in obj_ids:
            inner_ids = inner_ids + [res for res in inner_model.select(getattr(inner_model, "id")).where(
                getattr(inner_model, val) == obj_id)]
        # get ids or data from next table in chain
        data = recursive_filter(inner_model_name, keys[i + 1:], inner_ids, parent_model)
        return data


def get_many_data(model, values):
    """
    Return data for many_to_many mode

    :param model: table object
    :param values: values for filter

    :return: data
    """
    data = []
    child_name = values['child']
    del values['child']
    group_field = None
    if 'group_field' in values.keys():
        group_field = values['group_field']
        del values['group_field']
    # data for many_to_many with checked field
    if hasattr(model, child_name):
        condition = get_condition(model, values)
        if condition:
            data = get_child_data(model, child_name, condition)
    # group data for radiobutton
    if group_field:
        data = get_group_data(group_field, data)
    return data


def get_child_data(model, child_name, condition) -> list:
    """
    Return checked ids for many_to_many mode

    :param model: table object
    :param child_name: child table name
    :param condition: filter for parent, where parent_value_id == select_id

    :return: child_all_data
    """
    # get child table object from foreign link
    child_model = getattr(model, child_name).rel_model
    # get all records from child table
    child_all_data = [row for row in child_model.select().dicts()]
    # get select records
    child_select_data = [row for row in model.select(getattr(model, child_name)).where(condition).dicts()]
    # get select ids
    select_ids = [row_value[child_name] for row_value in child_select_data]
    # add checked field value
    if child_all_data:
        for child_data in child_all_data:
            if child_data['id'] in select_ids:
                child_data['checked'] = True
            else:
                child_data['checked'] = False
    return child_all_data


def get_group_data(group_field, data) -> list:
    """
    Return checked ids for many_to_many mode

    :param group_field: field for group radiobutton
    :param data: data before apply many_to_many mode with checked field

    :return: res_data
    [
        {
            "group_label": display name for group,
            "items":
                [

                ]
        },
        ...
    ]
    """
    group_data = [row for row in get_model(group_field).select()]
    res_data = []
    for group_row in group_data:
        items = {"group_label": group_row.name}
        items_data = []
        for child_data in data:
            if child_data[group_field] == group_row.id:
                items_data.append(child_data)
        items["items"] = items_data
        res_data.append(items)
    return res_data


def create_sidebar() -> list:
    """
    Return information for sidebar from cache

    :return: data
    """
    data = []
    for table_name in cache.get_sidebar_fields():
        table_info = cache.get_table_info(table_name).get()
        data.append({"title": table_info.title, "icon": table_info.icon, "name": table_info.name})
    return data


def get_dicts_info() -> list:
    """
    Return displayed titles for all tables from cache

    :return: data
    """
    all_table_info = cache.get_table_info_model().select()
    data = []
    for table_info in all_table_info:
        value = {"name": table_info.name, "title": table_info.title}
        data.append(value)
    return data


def get_dict_info(collection, params) -> dict:
    """
    Collects all parameters for table display

    :param collection: table name
    :param params: dict with parameters

    :return: data
    """
    table_info = cache.get_table_info(collection).get()
    model = get_model(collection)
    data = {}
    # get parent name from params for many_to_many mode
    parent_name = None
    if 'parent' in params.keys():
        parent_name = params['parent']

    data["title"] = table_info.title
    if table_info.many_to_many:
        data['mode'] = 'many_to_many'
    if table_info.group_field:
        data['group_field'] = table_info.group_field

    fields = []
    for field_name in model._meta.fields:
        # exclude fields that are not displayed
        if field_name in ('id', 'uuid', 'version_number', parent_name):
            continue
        field_object = getattr(model, field_name)
        if table_info.many_to_many and parent_name:
            if field_name != parent_name:
                # only name field for the column in many_to_many mode
                fields.append({"key": "name", "label": field_object.verbose_name})
                # add a parameter 'child' with the name of the child table
                data['child'] = field_name
            continue
        field_info = {"key": field_name, "label": field_object.verbose_name}
        if field_name == 'name':
            field_info["sortable"] = True
        if isinstance(field_object, ForeignKeyField):
            field_info["type"] = "selectable"
        if isinstance(field_object, DoubleField):
            field_info["type"] = "float"
        if isinstance(field_object, IntegerField):
            field_info["type"] = "integer"
        if isinstance(field_object, BooleanField):
            field_info["type"] = "boolean"
        if isinstance(field_object, DateField):
            field_info["type"] = "date"
        fields.append(field_info)
    data["fields"] = fields

    filters = []
    filter_info_model = cache.get_filter_info_model()
    filters_info = filter_info_model.select().where(filter_info_model.table == table_info) \
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
