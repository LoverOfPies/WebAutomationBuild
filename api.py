from flask import jsonify, make_response, request, send_from_directory
from flask_cors import cross_origin
from werkzeug.exceptions import abort

from app import app
from src.db.DbUtils import get_model_by_name


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/v0.1/get/<string:collection>', methods=['GET'])
@cross_origin()
def get_data(collection):
    model = get_model_by_name(collection)
    if model is None:
        abort(404)
    data = [row for row in model.select().dicts()]
    return jsonify(data)


@app.route('/api/v0.1/add', methods=['POST'])
def add_value():
    if not request.json:
        abort(400)
    print(request.json['city'])  # формат какой?
    return jsonify('test', 201)


@app.route('/api/v0.1/update', methods=['PUT'])
def edit_value():
    # Если такой записи в таблице нет, то abort(400)
    # Всё норм? Вставляем значения полученные. Согласовать формат данных
    return jsonify({'result': True})  # что возвращаем?


@app.route('/api/v0.1/delete', methods=['DELETE'])
def delete_value():
    # Если записей в таблице нет, то abort(400)
    # Всё норм? удаляем запись. Согласовать формат данных
    return jsonify({'result': True})
