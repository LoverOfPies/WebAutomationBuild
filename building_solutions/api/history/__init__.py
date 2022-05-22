from flask import Blueprint, jsonify
from flask_cors import cross_origin

from api import __version__ as api_version
from api.history import HistoryImpl

history_api = Blueprint('history_api', __name__)


@history_api.route(f'{api_version}/get_history/<string:collection>/<int:id_row>', methods=['GET'])
@cross_origin()
def get_history(collection, id_row):
    data = HistoryImpl.get_history(collection, id_row)
    return jsonify(data)


@history_api.route(f'{api_version}/get_history_dict/<string:collection>', methods=['GET'])
@cross_origin()
def get_history_dict(collection):
    data = HistoryImpl.get_history_dict_info(collection)
    return jsonify(data)
