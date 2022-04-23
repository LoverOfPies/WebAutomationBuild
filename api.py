from flask import jsonify, make_response, request, send_from_directory, send_file, g
from flask_cors import cross_origin
from werkzeug.exceptions import abort

from MyAppException import MyAppException
import migrations
from app import app
from src.expimp import ExportImportUtils
import src.ApiUtils
import src.EstimateUtils

api_version = '/api/v0.1'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(MyAppException)
def http_error_handler(error):
    return make_response(jsonify({'error': error.message}), 500)


# TODO: Почему path с одним слешем не работает ???
@app.route('/', defaults={'path': ''})
@app.route('/dict/<path:path>')
@app.route('/settings')
def index(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route(f'{api_version}/get/<string:collection>', methods=['GET'])
@cross_origin()
def get_data(collection):
    """
    Get records from table

    :param collection: table name

    request.args
    --- mode: (optional) mode value
    --- child: (optional) table child name for many_to_many mode
    --- group_field: (optional) group field for radiobutton
    --- values:
    {
        'field': 'value',
        ...
    }

    :return: json
    ..code-block:: json
    [
        {
            'field': 'value',
            ...
        },
        ...
    ]
    """
    data = src.ApiUtils.get_data_from_table(collection, request.args)
    return jsonify(data)


@app.route(f'{api_version}/add/<string:collection>', methods=['POST'])
@cross_origin()
def add_value(collection):
    """
    Add record in table

    :param collection: table name

    request.json
    {
        'field': 'value',
        ...
    }

    :return: json
    ..code-block:: json
    [
        {
            'field': 'value',
            ...
        }
    ]
    """
    result = src.ApiUtils.add_row(collection, request.json)
    if result:
        # TODO: Костыль [0]
        data = [row for row in result.dicts()][0]
        return jsonify(data)
    return abort(404)


@app.route(f'{api_version}/update/<string:collection>/<int:id_row>', methods=['PUT'])
@cross_origin()
def edit_value(collection, id_row):
    """
    Update record in table

    :param collection: table name
    :param id_row: record id, for many_to_many child id

    request.json
    {
        'field': 'update field name'
        'value': 'update field value'
        'mode': (optional) 'mode name'
        'parent': (optional) 'parent table name for many_to_many'
        'parent_id': (optional) 'parent record id for many_to_many'
        'child': (optional) 'child table name for many_to_many'
        'prev': (optional) 'prev value for radiobutton'
        'current': (optional) 'current value for radiobutton'
    }

    :return: json
    """
    if not request.json:
        abort(400)
    result = src.ApiUtils.update_row(collection, id_row, request.json)
    if result:
        return jsonify({'result': True})
    return abort(404)


@app.route(f'{api_version}/delete/<string:collection>/<int:id_row>', methods=['DELETE'])
@cross_origin()
def delete_value(collection, id_row):
    """
    Delete record from a table by id

    :param collection: table name
    :param id_row: record id

    :return: json
    """
    result = src.ApiUtils.delete_row(collection, id_row)
    if result:
        return jsonify({'result': True})
    return abort(404)


# TODO: разбить на несколько методов
# К примеру, если у таблицы есть фильтры, отдавать признак
# После чего уже запрашивать фильтры
# С действиями возможно так же
@app.route(f'{api_version}/get_dict/<string:collection>', methods=['GET'])
@cross_origin()
def get_dict(collection):
    """
    Returns json with information about all tables for visibility

    :param collection: table name in Database

    request.args
    --- parent: (optional) parent name for many_to_many mode

    :return: json
    ..code-block:: json
    {
        "title": "display table name",
        "mode": "mode name",
        "child": "child table name",    # only many_to_many mode
        "group_field": "name fi",
        "fields": [
            {
                "key": "field name",
                "label": "display field name",
                "type": "selectable/float/integer/boolean/date",
                "sortable": "True/False"    # column sorting attribute
            },
            ...
        ],
        "filters": [
            {
                "key": "filter table",
                "label": "display name for filter table",
                "multiple": "plural display name for filter table"
            },
            ...
        ],
        "actions": [
            {
                "action": "route",
                "label": "display name for open table name",
                "to": "open table name"
            },
            ...
        ]
    }
    """
    data = src.ApiUtils.get_dict_info(collection, request.args)
    return jsonify(data)


@app.route(f'{api_version}/get_dict', methods=['GET'])
@cross_origin()
def get_dicts():
    """
    Returns json with information about all tables for visibility

    :return: return json
    ..code-block:: json
    [
        {
        "name": "table name",
        "title": "display name"
        },
        ...
    ]
    """
    data = src.ApiUtils.get_dicts_info()
    return jsonify(data)


@app.route(f'{api_version}/sidebar', methods=['GET'])
@cross_origin()
def get_sidebar():
    """
    Returns json with information to display the sidebar

    :return: return json
    ..code-block:: json
    [
        {
            "icon": "bootstrap icon name",
            "name": "table name",
            "title": "display name"
        },
        ...
    ]
    """
    sidebar = src.ApiUtils.create_sidebar()
    return jsonify(sidebar)


@app.route(f'{api_version}/import/<string:collection>', methods=['POST'])
@cross_origin()
def file_import(collection):
    if request.method == 'POST':
        # path = ExportImportUtils.save_file(request.files)
        # if path is None:
        #     abort(404)
        res = ExportImportUtils.import_single_table(collection)
        if not res:
            abort(404)
    return jsonify('True')


@app.route(f'{api_version}/export/<string:collection>', methods=['GET'])
@cross_origin()
def file_export(collection):
    ExportImportUtils.export_table(collection)
    return jsonify('True')


@app.route(f'{api_version}/get_estimate_records', methods=['GET'])
@cross_origin()
def get_estimate_records():
    data = src.EstimateUtils.get_estimate_records()
    return jsonify(data)


@app.route(f'{api_version}/calculate_estimate/<int:id_estimate>', methods=['POST'])
@cross_origin()
def calculate_estimate(id_estimate):
    """

    :return:
    """
    # Принимаем json { client_fio, use_base, project_id
    # additional_works: [1, 2, ...] (optional),
    # work_technologies: [1, 2, ...] (optional) }
    src.EstimateUtils.calculate_estimate(id_estimate, request.json)
    return jsonify('True')


@app.route(f'{api_version}/delete_estimate/<int:id_estimate>', methods=['DELETE'])
@cross_origin()
def delete_estimate(id_estimate):
    src.EstimateUtils.delete_estimate(id_estimate)
    return jsonify('True')


@app.route(f'{api_version}/edit_estimate/<int:id_estimate>', methods=['PUT'])
@cross_origin()
def edit_estimate(id_estimate):
    # Принимаем json { client_fio, use_base, project_id
    # additional_works: [1, 2, ...] (optional),
    # work_technologies: [1, 2, ...] (optional) }
    src.EstimateUtils.edit_estimate(id_estimate, request.json)
    return jsonify('True')


@app.route(f'{api_version}/get_estimate_materials/<int:id_estimate>', methods=['GET'])
@cross_origin()
def get_estimate_materials(id_estimate):
    data = src.EstimateUtils.get_estimate_materials(id_estimate)
    return jsonify(data)


@app.route(f'{api_version}/get_estimate_works/<int:id_estimate>', methods=['GET'])
@cross_origin()
def get_estimate_works(id_estimate):
    data = src.EstimateUtils.get_estimate_works(id_estimate)
    return jsonify(data)


@app.route(f'{api_version}/export_estimate/<int:id_estimate>', methods=['GET'])
@cross_origin()
def export_estimate(id_estimate):
    src.EstimateUtils.export_estimate(id_estimate)
    return jsonify('True')


@app.route(f'{api_version}/get_project_technologies/<int:id_project>', methods=['GET'])
@cross_origin()
def get_project_technologies(id_project):
    data = src.EstimateUtils.get_project_technologies(id_project)
    return jsonify(data)


@app.route(f'{api_version}/create_estimate/', methods=['GET'])
@cross_origin()
def create_estimate():
    estimate_id = src.EstimateUtils.create_estimate()
    return jsonify(estimate_id)


@app.route(f'{api_version}/copy_work_group/<int:id_work_group>', methods=['GET'])
@cross_origin()
def copy_work_group(id_work_group):
    new_work_group = src.ApiUtils.copy_work_group(id_work_group)
    return jsonify(new_work_group)
