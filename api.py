from flask import jsonify, make_response, request, send_from_directory, send_file
from flask_cors import cross_origin
from werkzeug.exceptions import abort

from app import app
from src.utils import get_model, delete_row, update_row, add_row, create_sidebar, get_dict_info, save_file, \
    create_file, get_condition, get_dicts_info, get_filter_data
from src.expimp.ImportUtils import import_single_table, import_custom_data

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
    if request.args:
        if "mode" in request.args.keys():
            data = get_filter_data(model, request.args)
            return jsonify(data)
    condition = get_condition(model, request.args)
    if condition:
        data = [row for row in model.select().where(condition).dicts()]
    else:
        data = [row for row in model.select().dicts()]
    return jsonify(data)


@app.route(f'{api_version}/add/<string:collection>', methods=['POST'])
@cross_origin()
def add_value(collection):
    result = add_row(collection, request.json)
    if result:
        data = [row for row in result.dicts()]
        return jsonify(data)
    return abort(404)


@app.route(f'{api_version}/update/<string:collection>/<int:id_row>', methods=['PUT'])
@cross_origin()
def edit_value(collection, id_row):
    if not request.json:
        abort(400)
    result = update_row(collection, id_row, request.json)
    if result:
        return jsonify({'result': True})
    return abort(404)


@app.route(f'{api_version}/delete/<string:collection>/<int:id_row>', methods=['DELETE'])
@cross_origin()
def delete_value(collection, id_row):
    result = delete_row(collection, id_row)
    if result:
        return jsonify({'result': True})
    return abort(404)


@app.route(f'{api_version}/get_dict/<string:collection>', methods=['GET'])
@cross_origin()
def get_dict(collection):
    data = get_dict_info(collection)
    return jsonify(data)


@app.route(f'{api_version}/get_dict', methods=['GET'])
@cross_origin()
def get_dicts():
    data = get_dicts_info()
    return jsonify(data)


@app.route(f'{api_version}/sidebar', methods=['GET'])
@cross_origin()
def get_sidebar():
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
