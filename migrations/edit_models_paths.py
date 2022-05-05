from api.base.DataBaseUtils import cache


def run_script():
    try:
        table_info_model = cache.get_table_info_model()
        table_info_records = [row for row in table_info_model.select()]
        for row in table_info_records:
            field_data = dict(row.__data__)
            field_data['path'] = row.path.replace('src.', '')
            query = table_info_model.update(**field_data).where(table_info_model.id == row.id)
            query.execute()
        return True
    except:
        return False
