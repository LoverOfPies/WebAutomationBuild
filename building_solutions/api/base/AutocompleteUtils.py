import copy
import datetime

from api.base import DataBaseUtils


def base_size_autocomplete(project_id):
    base_size_model = DataBaseUtils.get_model('base_size')
    data = {'project': project_id}
    base_units = DataBaseUtils.get_records(DataBaseUtils.get_model('base_unit'))
    for base_unit in base_units:
        data['base_unit'] = base_unit
        DataBaseUtils.get_or_insert(base_size_model, data)


def base_size_cascade_delete(delete_row, collection):
    base_size_model = DataBaseUtils.get_model('base_size')
    base_sizes = DataBaseUtils.get_records(base_size_model, {collection: delete_row})
    for base_size in base_sizes:
        DataBaseUtils.delete_record(base_size_model, base_size)


def product_autocomplete(material_id):
    product_model = DataBaseUtils.get_model('product')
    data = {'material': material_id,
            'amount_for_one': 0,
            'price': 0,
            'date_version': datetime.datetime.now()}
    DataBaseUtils.get_or_insert(product_model, data)


def material_cascade_delete(material):
    product_model = DataBaseUtils.get_model('product')
    products = DataBaseUtils.get_records(product_model, {'material': material})
    for product in products:
        DataBaseUtils.delete_record(product_model, product)


def create_new_version(model, row, data):
    field_data = dict(row.__data__)
    new_data = copy.deepcopy(field_data)
    del new_data['id']
    new_data[data['field']] = data['value']
    new_data['version_number'] = new_data['version_number'] + 1
    new_data['date_version'] = datetime.datetime.now()
    DataBaseUtils.insert_record(model, new_data)
    field_data['enable_version'] = False
    query = model.update(**field_data).where(model.id == row.id)
    query.execute()
