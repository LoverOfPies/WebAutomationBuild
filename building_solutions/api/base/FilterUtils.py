from peewee import Model


def get_equals_filter(model: Model, values: dict):
    """
    Return equals filter by fields and values
    format: {"field": value, ...}

    :param model: table object
    :param values: fields and values for filter

    :return: filter
    """
    if not values:
        return None
    filters = []
    for field, filter_value in values.items():
        if hasattr(model, field):
            filter_field = getattr(model, field)
            filters.append(filter_field == filter_value)
    condition = None
    for i, filter_obj in enumerate(filters):
        if i == 0:
            condition = filter_obj
            continue
        condition = condition & filter_obj
    return condition
