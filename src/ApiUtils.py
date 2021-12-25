from peewee import ForeignKeyField, DoubleField, IntegerField, BooleanField, DateField

from src import FilterUtils
from src.db import DataBaseUtils


def add_row(collection, data):
    """
    Add record in table

    :param collection: table name
    :param data: fields and values

    :return: new record or None
    """
    model = DataBaseUtils.get_model(collection)
    if model is None:
        return None
    if not DataBaseUtils.check_data(data, model):
        return None
    if collection == 'work' and 'work_base' not in data:
        data['work_base'] = False
    obj, meth = DataBaseUtils.get_or_insert(model, data)
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
    model = DataBaseUtils.get_model(collection)
    if model is None:
        return False
    row = model.get_or_none(id=id_row)
    if row is None:
        return False
    return DataBaseUtils.delete_record(model, row)


def update_row(collection, id_row, data) -> bool:
    """
    Update record field by id

    :param collection: table name
    :param id_row: record id
    :param data: dict with request parameters

    :return: bool
    """
    model = DataBaseUtils.get_model(collection)
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
                    obj = DataBaseUtils.get_record(model, values)
                    obj.delete_instance()
                if current != -1:
                    values = {parent: parent_id, child: current}
                    DataBaseUtils.insert_record(model, values)
            # classic many_to_many
            # add or remove record when switching checkbox
            else:
                child_id = id_row
                checked = data['value']
                values = {parent: parent_id, child: child_id}
                if checked:
                    DataBaseUtils.insert_record(model, values)
                else:
                    obj = DataBaseUtils.get_record(model, values)
                    obj.delete_instance()
            return True

    return DataBaseUtils.update_record(model, id_row, data)


def get_data_from_table(collection, request_params):
    model = DataBaseUtils.get_model(collection)
    if model is None:
        return None
    data = None
    if request_params:
        values = dict(request_params)
        if 'mode' in values.keys():
            # get data for chain filter in grid
            if values['mode'] == 'advanced_filters':
                del values['mode']
                return get_filter_data(model, values)
            # get data for many_to_many mode
            if values['mode'] == 'many_to_many':
                del values['mode']
                return get_many_data(model, values)
        else:
            # get data with filter by fields
            condition = FilterUtils.get_equals_filter(model, values)
            if condition:
                data = [row for row in model.select().where(condition).dicts()]
    else:
        # get all records from table
        data = [row for row in model.select().dicts()]
    return data


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
            inner_model = DataBaseUtils.get_model(inner_model_name)
            inner_ids = [inner_id for inner_id in inner_model.select(getattr(inner_model, "id")).where(
                getattr(inner_model, model_name) == values[model_name])]
            data = recursive_filter(inner_model_name, keys[i + 1:], inner_ids, model)
            return data


# TODO: Rewrite to FilterUtils
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
        inner_model = DataBaseUtils.get_model(inner_model_name)
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
        condition = FilterUtils.get_equals_filter(model, values)
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
    group_data = [row for row in DataBaseUtils.get_model(group_field).select()]
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
    for table_name in DataBaseUtils.cache.get_sidebar_fields():
        table_info = DataBaseUtils.cache.get_table_info(table_name).get()
        data.append({"title": table_info.title, "icon": table_info.icon, "name": table_info.name})
    return data


def get_dicts_info() -> list:
    """
    Return displayed titles for all tables from cache

    :return: data
    """
    all_table_info = DataBaseUtils.cache.get_table_info_model().select()
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
    table_info = DataBaseUtils.cache.get_table_info(collection).get()
    model = DataBaseUtils.get_model(collection)
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
    filter_info_model = DataBaseUtils.cache.get_filter_info_model()
    filters_info = filter_info_model.select().where(filter_info_model.table == table_info) \
        .order_by(filter_info_model.id.asc())
    for filter_info in filters_info:
        filters.append({"key": filter_info.key, "label": filter_info.label, "multiple": filter_info.multiple})
    data["filters"] = filters

    actions = []
    action_info_model = DataBaseUtils.cache.get_action_info_model()
    actions_info = action_info_model.select().where(action_info_model.table == table_info)
    for action_info in actions_info:
        actions.append({"action": action_info.action, "label": action_info.label, "to": action_info.to})
    data["actions"] = actions

    return data


def get_estimate_records():
    model = DataBaseUtils.get_model('estimate')
    if model is None:
        return None
    return [row for row in model.select().dicts()]


def calculate_estimate(data):
    estimate_model = DataBaseUtils.get_model('estimate')
    if estimate_model is None:
        return
    fio = data['client_info']
    use_base = data['use_base']
    # Проект не обязательный
    project_id = None
    if 'project_id' in data.keys():
        project_id = data['project_id']
    # Создаём расчёт чтобы заполнить связки
    estimate_data = dict([('client_fio', fio), ('use_base', use_base)])
    if project_id:
        estimate_data['project'] = project_id
    estimate, meth = DataBaseUtils.get_or_insert(estimate_model, estimate_data)
    # Проставляем номер равный id
    DataBaseUtils.update_record(estimate_model, estimate,
                                dict([('field', 'number'), ('value', estimate)]))
    # Получаем технологии для расчёта кастомные или из проекта
    estimate_technologies_model = DataBaseUtils.get_model('estimate_technology')
    technologies_data = []
    if 'work_technologies' in data:
        estimate_technologies = data['work_technologies']
        technologies_data = [dict([('estimate', estimate), ('work_technology', work_technology_id)])
                             for work_technology_id in estimate_technologies]
    else:
        project_technology_model = DataBaseUtils.get_model('project_technology')
        technologies_project = DataBaseUtils.get_records(project_technology_model, ({'project': project_id}))
        work_technologies = []
        for technology_project in technologies_project:
            work_technologies.append(technology_project.work_technology)
        technologies_data = [dict([('estimate', estimate), ('work_technology', work_technology.id)])
                             for work_technology in work_technologies]
    # Собираем работы из технологий
    works = set()
    work_model = DataBaseUtils.get_model('work')
    for technology in technologies_data:
        technologies_obj, _ = DataBaseUtils.get_or_insert(estimate_technologies_model, technology)
        technology_group_model = DataBaseUtils.get_model('technology_group')
        tech_groups = DataBaseUtils.get_records(technology_group_model,
                                                ({'work_technology': technology['work_technology']}))
        for tech_group in tech_groups:
            tech_group_objects = DataBaseUtils.get_records(technology_group_model,
                                                           ({'work_group': tech_group.work_group.id}))
            for tech_group_object in tech_group_objects:
                works.update(DataBaseUtils.get_records(work_model, ({'work_group': tech_group_object.work_group.id})))
    # Собираем дополнительные работы
    if 'additional_works' in data:
        additional_model = DataBaseUtils.get_model('estimate_additional')
        additional_works = data['additional_works']
        additional_data = [dict([('estimate', estimate), ('work', work_id)]) for work_id in additional_works]
        for additional in additional_data:
            additional_work_id, _ = DataBaseUtils.get_or_insert(additional_model, additional)
            additional_work_object = DataBaseUtils.get_record(work_model, ({'id': additional['work']}))
            works.add(additional_work_object)
    # Обрабатываем работы
    estimate_price_client = 0
    estimate_price_base = 0
    estimate_work_model = DataBaseUtils.get_model('estimate_work')
    base_size_model = DataBaseUtils.get_model('base_size')
    for work_object in works:
        work_client_price = 0
        work_base_price = 0
        if work_object.work_coefficient != 0:
            base_size = DataBaseUtils.get_record(base_size_model,
                                                 ({'project': project_id, 'base_unit': work_object.base_unit}))
            work_client_price = (work_object.work_coefficient * work_object.client_price * base_size.amount)
            work_base_price = (work_object.work_coefficient * work_object.work_price * base_size.amount)
        else:
            work_client_price = work_object.client_price
            work_base_price = work_object.work_price
        # Добавляем работу в EstimateWork
        work_data = dict([('estimate', estimate), ('work', work_object.id),
                          ('client_price', work_client_price), ('base_price', work_base_price)])
        DataBaseUtils.get_or_insert(estimate_work_model, work_data)
        estimate_price_client += work_client_price
        estimate_price_base += work_base_price
    # Заполняем цены для расчёта
    DataBaseUtils.update_record(estimate_model, estimate,
                                dict([('field', 'price_base'), ('value', estimate_price_base)]))
    # Обрабатываем материалы
    work_material_model = DataBaseUtils.get_model('work_material')
    product_model = DataBaseUtils.get_model('product')
    estimate_work_model = DataBaseUtils.get_model('estimate_material')
    for work in works:
        work_material_data = DataBaseUtils.get_records(work_material_model,
                                                       ({'work': work.id}))
        for work_material in work_material_data:
            base_size = DataBaseUtils.get_record(base_size_model,
                                                 ({'project': project_id, 'base_unit': work_material.work.base_unit}))
            product_obj = DataBaseUtils.get_record(product_model, ({'material': work_material.material.id}))
            material_price = \
                ((work_material.amount * base_size.amount) / product_obj.amount_for_one) * product_obj.price
            estimate_material_data = dict([('estimate', estimate), ('product', product_obj.id),
                                           ('price', material_price)])
            DataBaseUtils.get_or_insert(estimate_work_model, estimate_material_data)
            estimate_price_client += material_price
    DataBaseUtils.update_record(estimate_model, estimate,
                                dict([('field', 'price_client'), ('value', estimate_price_client)]))


def get_estimate_materials(id_estimate):
    pass


def get_estimate_works(id_estimate):
    model = DataBaseUtils.get_model('estimate_work')
    if model is None:
        return None
    data = [row for row in model.select().where(model.estimate == id_estimate).dicts()]
    work_model = DataBaseUtils.get_model('work')
    for value in data:
        work = DataBaseUtils.get_record(work_model, {'id': value['work']})
        value['work_name'] = work.name
    return data


def export_estimate(id_estimate):
    pass
