from api.base import DataBaseUtils, FilterUtils


def get_history(collection, id_row):
    model = DataBaseUtils.get_model(collection)
    row = model.get_or_none(id=id_row)
    condition = FilterUtils.get_equals_filter(model, {'uuid': row.uuid})
    data = [row for row in model.select().where(condition).dicts()]
    return data


def get_history_dict_info(collection) -> dict:
    table_info = DataBaseUtils.cache.get_table_info(collection).get()
    model = DataBaseUtils.get_model(collection)
    data = {'title': f'История изменений {table_info.title}'}
    fields = []
    for field_name in model._meta.fields:
        # exclude fields that are not displayed
        if field_name in ('id', 'uuid'):
            continue
        field_object = getattr(model, field_name)
        field_info = {"key": field_name,
                      "label": field_object.verbose_name,
                      "type": DataBaseUtils.get_field_type(field_object)}
        fields.append(field_info)
    data["fields"] = fields
    return data
