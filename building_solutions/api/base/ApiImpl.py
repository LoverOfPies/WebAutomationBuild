from typing import List

from api.base.MyAppException import MyAppException
from api.base import FilterUtils
from api.base import AutocompleteUtils
from api.base import DataBaseUtils
from api.base.DataBaseUtils import GET_METH, ERROR_METH


def add_row(collection, data):
    """
    Add record in table

    :param collection: table name
    :param data: fields and values

    :return: new record or None
    """
    # TODO: добавить обозначение в моделях, какие поля обязательны к уникальности
    #  метод get
    model = DataBaseUtils.get_model(collection)
    for field in data:
        if not hasattr(model, field):
            raise MyAppException('Неправильно переданы поля модели')
    obj, meth = DataBaseUtils.get_or_insert(model, data)
    if meth == "get":
        raise MyAppException('Похожая запись уже существует')
    # TODO: Переделать механизм автозаполнения
    if collection == 'project' or collection == 'base_unit':
        AutocompleteUtils.base_size_autocomplete(obj)
    if collection == 'material':
        AutocompleteUtils.base_size_autocomplete(obj)
        AutocompleteUtils.product_autocomplete(obj)
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
    row = model.get_or_none(id=id_row)
    # TODO: Переделать механизм автозаполнения
    if collection == 'base_unit' or collection == 'project':
        AutocompleteUtils.base_size_cascade_delete(row, collection)
    if collection == 'material':
        AutocompleteUtils.material_cascade_delete(row)
    return DataBaseUtils.delete_record(model, row)


# TODO: Переписать
def update_row(collection, id_row, data) -> bool:
    """
    Update record field by id

    :param collection: table name
    :param id_row: record id
    :param data: dict with request parameters

    :return: bool
    """
    model = DataBaseUtils.get_model(collection)
    if 'mode' in data:
        if data['mode'] == 'many_to_many':
            parent = data['parent']
            parent_id = data['parent_id']
            child = data['child']
            # radiobutton change
            # current = -1 - remove flag
            # prev = -1 - first init
            if 'prev' in data:
                prev = data['prev']
                current = data['current']
                if prev != -1:
                    values = {parent: parent_id, child: prev}
                    obj = DataBaseUtils.get_record(model, values)
                    obj.delete_instance()
                if current != -1:
                    values = {parent: parent_id, child: current}
                    DataBaseUtils.get_or_insert(model, values)
            # classic many_to_many
            # add or remove record when switching checkbox
            else:
                child_id = id_row
                checked = data['value']
                values = {parent: parent_id, child: child_id}
                if checked:
                    DataBaseUtils.get_or_insert(model, values)
                else:
                    obj = DataBaseUtils.get_record(model, values)
                    obj.delete_instance()
            return True

    return DataBaseUtils.update_record(collection, id_row, data)


# TODO: Переписать
def get_data_from_table(collection, request_params):
    model = DataBaseUtils.get_model(collection)
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
    # Очередное некрасивое решение для версионности
    if data and 'enable_version' in data[0]:
        data = [row for row in data if row['enable_version']]
    # Очередное некрасивое решение
    if collection == 'product':
        for row_dict in data:
            material_model = DataBaseUtils.get_model('material')
            row_material = material_model.get_or_none(id=row_dict['material'])
            row_dict['unit'] = row_material.unit.name
    return data


# TODO: Переписать
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


# TODO: Разнести на два метода get_group_data и get_many_data
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
    group_field = values('group_field', None)
    if group_field:
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


def create_sidebar() -> List[dict]:
    """
    Return information for sidebar from cache

    :return: data
    """
    data = []
    for table_name in DataBaseUtils.cache.get_sidebar_fields():
        table_info = DataBaseUtils.cache.get_table_info(table_name).get()
        data.append({"title": table_info.title, "icon": table_info.icon, "name": table_info.name})
    return data


def get_dicts_info() -> List[dict]:
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
    parent_name = params.get('parent', None)

    data["title"] = table_info.title
    if table_info.many_to_many:
        data['mode'] = 'many_to_many'
    if table_info.group_field:
        data['group_field'] = table_info.group_field

    fields = []
    for field_name in model._meta.fields:
        # exclude fields that are not displayed
        if field_name in ('id', 'uuid', 'version_number', 'enable_version', parent_name):
            continue
        field_object = getattr(model, field_name)

        # TODO: Вынести, подумать над работой режимов
        if table_info.many_to_many and parent_name:
            if field_name != parent_name:
                # only name field for the column in many_to_many mode
                fields.append({"key": "name", "label": field_object.verbose_name})
                # add a parameter 'child' with the name of the child table
                data['child'] = field_name
            continue

        field_info = {"key": field_name,
                      "label": field_object.verbose_name,
                      "type": DataBaseUtils.get_field_type(field_object)}
        fields.append(field_info)

        # TODO: Костыль, надо убрать
        if collection == 'product' and field_name == "amount_for_one":
            fields.append({"key": "unit", "type": "caption", "label": "Единицы измерения"})

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


# TODO: Вынести функционал и переработать интерфейс
def copy_work_group(id_work_group):
    # Получаем родительскую группу работ
    work_group_model = DataBaseUtils.get_model('work_group')
    parent_work_group = DataBaseUtils.get_record(work_group_model, {'id': id_work_group})

    # Создаём новую группу работ
    new_work_group, meth = DataBaseUtils.get_or_insert(work_group_model,
                                                       {'name': f'{parent_work_group.name} (Копия)',
                                                        'work_stage': parent_work_group.work_stage})
    if meth in (GET_METH, ERROR_METH):
        if new_work_group:
            raise MyAppException('Уже есть копия данного объекта, отредактируйте её')
        raise MyAppException('Ошибка создания копии, оформите задачу на исправление')

    # Получаем работы привязанные к этой группе
    work_model = DataBaseUtils.get_model('work')
    parent_works = DataBaseUtils.get_records(work_model, {'work_group': id_work_group})

    # Создаём новые работы
    for parent_work in parent_works:
        new_work, meth = DataBaseUtils.get_or_insert(work_model,
                                                     {'work_group': new_work_group,
                                                      'name': f'{parent_work.name} ({parent_work_group.name})',
                                                      'fix_price': parent_work.fix_price,
                                                      'client_price': parent_work.client_price,
                                                      'work_price': parent_work.work_price,
                                                      'work_base': parent_work.work_base,
                                                      'base_unit': parent_work.base_unit.id})

        # Получаем используемые в работе материалы
        work_material_model = DataBaseUtils.get_model('work_material')
        parent_work_materials = DataBaseUtils.get_records(work_material_model, {'work': parent_work.id})

        # Задаём для новых работ используемые материалы
        for parent_work_material in parent_work_materials:
            DataBaseUtils.get_or_insert(work_material_model,
                                        {'work': new_work,
                                         'material_coefficient': parent_work_material.material_coefficient,
                                         'amount': parent_work_material.amount,
                                         'material': parent_work_material.material.id})

    # Возвращаем созданную запись
    return work_group_model.get_or_none(id=new_work_group).__data__
