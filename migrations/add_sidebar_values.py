from api.base.DataBaseUtils import cache

SIDEBAR = [
    "prop",
    "unit",
    "material",
    "product",
    "work",
    "work_technology",
    "base_unit",
    "project"
]


def run_script():
    try:
        table_info_model = cache.get_table_info_model()
        table_info_records = [row for row in table_info_model.select().where(table_info_model.name.in_(SIDEBAR))]
        for row in table_info_records:
            field_data = dict(row.__data__)
            field_data['show_in_sidebar'] = True
            query = table_info_model.update(**field_data).where(table_info_model.id == row.id)
            query.execute()
        return True
    except:
        return False
