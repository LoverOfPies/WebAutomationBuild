from flask import jsonify, make_response, request, send_from_directory, send_file
from flask_cors import cross_origin
from werkzeug.exceptions import abort

from app import app
from src.expimp.ExportImportUtils import import_single_table, import_custom_data, save_file, create_file
from src.utils import get_model, delete_row, update_row, add_row, create_sidebar, get_dict_info, \
    get_condition, get_dicts_info, get_filter_data, get_many_data

api_version = '/api/v0.1'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route(f'{api_version}/get/<string:collection>', methods=['GET'])
@cross_origin()
def get_data(collection):
    model = get_model(collection)
    if model is None:
        abort(404)
    data = None
    if request.args:
        values = dict(request.args)
        if 'mode' in values.keys():
            if values['mode'] == 'advanced_filters':
                data = get_filter_data(model, values)
            if values['mode'] == 'many_to_many':
                data = get_many_data(model, values)
        else:
            condition = get_condition(model, values)
            if condition:
                data = [row for row in model.select().where(condition).dicts()]
    else:
        data = [row for row in model.select().dicts()]
    return jsonify(data)


@app.route(f'{api_version}/add/<string:collection>', methods=['POST'])
@cross_origin()
def add_value(collection):
    """
    Add record in table

    :param collection: table name

    :return: json
    ..code-block:: json
    [
        {
            
        },
        ...
    ]
    """
    result = add_row(collection, request.json)
    if result:
        data = [row for row in result.dicts()]
        return jsonify(data)
    return abort(404)


@app.route(f'{api_version}/update/<string:collection>/<int:id_row>', methods=['PUT'])
@cross_origin()
def edit_value(collection, id_row):
    """
    Update record in table

    :param collection: table name
    :param id_row: record id, for many_to_many child id

    request.params
    --- field: update field name
    --- value: update field value
    --- mode: (optional) mode name
    --- parent: (optional) parent table name for many_to_many
    --- parent_id: (optional) parent record id for many_to_many
    --- child: (optional) child table name for many_to_many
    --- prev: (optional) prev value for radiobutton
    --- current: (optional) current value for radiobutton

    :return: json
    """
    if not request.json:
        abort(400)
    result = update_row(collection, id_row, request.json)
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
    result = delete_row(collection, id_row)
    if result:
        return jsonify({'result': True})
    return abort(404)


@app.route(f'{api_version}/get_dict/<string:collection>', methods=['GET'])
@cross_origin()
def get_dict(collection):
    """
    Returns json with information about all tables for visibility

    :param collection: table name in Database

    request.params
    --- parent: (optional) parent name for many_to_many mode

    :return: json
    ..code-block:: json
    {
        "title": "display table name",
        "mode": "mode name",
        "child": "child table name",    # only many_to_many mode
        "group_field": "name field for radiobutton group", # only many_to_many mode
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
                "label": "display name for open table",
                "to": "open table name"
            },
            ...
        ]
    }
    """
    data = get_dict_info(collection, request.args)
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
    data = get_dicts_info()
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
    sidebar = create_sidebar()
    return jsonify(sidebar)


@app.route(f'{api_version}/import/<string:collection>', methods=['POST'])
@cross_origin()
def file_import(collection):
    model = get_model(collection)
    if model is None:
        abort(404)
    if request.method == 'POST':
        path = save_file(request.files)
        if path is None:
            abort(404)
        res = import_single_table(model, path)
        if not res:
            abort(404)
    return jsonify('True')


@app.route(f'{api_version}/export/<string:collection>', methods=['GET'])
@cross_origin()
def file_export(collection):
    path = create_file(collection)
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route(f'{api_version}/import', methods=['POST'])
@cross_origin()
def file_custom_import():
    if request.method == 'POST':
        path = save_file(request.files)
        if path is None:
            abort(404)
        res = import_custom_data(path)
        if res:
            return jsonify('True')
    abort(404)
