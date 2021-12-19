from flask import jsonify, make_response, request, send_from_directory, send_file, g
from flask_cors import cross_origin
from werkzeug.exceptions import abort

from app import app
from src.expimp import ExportImportUtils
import src.ApiUtils

api_version = '/api/v0.1'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# TODO: Почему path с одним слешем не работает ???
@app.route('/', defaults={'path': ''})
@app.route('/dict/<path:path>')
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
        path = ExportImportUtils.save_file(request.files)
        if path is None:
            abort(404)
        res = ExportImportUtils.import_single_table(collection, path)
        if not res:
            abort(404)
    return jsonify('True')


@app.route(f'{api_version}/export/<string:collection>', methods=['GET'])
@cross_origin()
def file_export(collection):
    path = ExportImportUtils.create_file(collection)
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route(f'{api_version}/import', methods=['POST'])
@cross_origin()
def file_custom_import():
    if request.method == 'POST':
        path = ExportImportUtils.save_file(request.files)
        if path is None:
            abort(404)
        res = ExportImportUtils.import_custom_data(path)
        if res:
            return jsonify('True')
    abort(404)
