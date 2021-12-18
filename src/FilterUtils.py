def get_equals_filter(model, values):
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
