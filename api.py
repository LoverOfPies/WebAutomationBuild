from flask import jsonify, make_response, request, send_from_directory
from flask_cors import cross_origin
from werkzeug.exceptions import abort

from app import app
from src.db.utils import get_model, delete_row, update_row, add_row, create_sidebar

api_version = '/api/v0.1/'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route(f'{api_version}get/<string:collection>', methods=['GET'])
@cross_origin()
def get_data(collection):
    model = get_model(collection)
    if model is None:
        abort(404)
    data = [row for row in model.select().dicts()]
    return jsonify(data)


@app.route(f'{api_version}add/<string:collection>', methods=['POST'])
def add_value(collection):
    result = add_row(collection, request.json)
    if result:
        return jsonify('True')
    return abort(404)


@app.route(f'{api_version}update/<string:collection>/<int:id_row>', methods=['PUT'])
def edit_value(collection, id_row):
    if not request.json:
        abort(400)
    result = update_row(collection, id_row, request.json)
    if result:
        return jsonify({'result': True})
    return abort(404)


@app.route(f'{api_version}delete/<string:collection>/<int:id_row>', methods=['DELETE'])
def delete_value(collection, id_row):
    result = delete_row(collection, id_row)
    if result:
        return jsonify({'result': True})
    return abort(404)


@app.route(f'{api_version}sidebar', methods=['GET'])
def get_sidebar():
    sidebar = create_sidebar()
    return jsonify(sidebar)
