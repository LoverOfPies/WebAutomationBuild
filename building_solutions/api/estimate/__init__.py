from flask import jsonify, request, Blueprint, Response
from flask_cors import cross_origin


import api.estimate.EstimateImpl
from api import __version__ as api_version

estimate_api = Blueprint('estimate_api', __name__)


@estimate_api.route(f'{api_version}/get_estimate_records', methods=['GET'])
@cross_origin()
def get_estimate_records():
    data = api.estimate.EstimateImpl.get_estimate_records()
    return jsonify(data)


@estimate_api.route(f'{api_version}/create_estimate/', methods=['GET'])
@cross_origin()
def create_estimate() -> Response:
    """
    Внешний метод для инициализации расчёта по кнопке "Добавить" на интерфейсе расчёта

    :return: estimate_id (int) - ид созданного расчёта
    """
    estimate_id: int = api.estimate.EstimateImpl.create_estimate()
    return jsonify(estimate_id)


@estimate_api.route(f'{api_version}/delete_estimate/<int:id_estimate>', methods=['DELETE'])
@cross_origin()
def delete_estimate(id_estimate: int) -> Response:
    """
    Внешний метод для удаления расчёта по кнопке "Удалить" на интерфейсе расчёта

    :param: id_estimate (int) ид расчёта
    """
    api.estimate.EstimateImpl.delete_estimate(id_estimate)
    return jsonify('True')


@estimate_api.route(f'{api_version}/calculate_estimate/<int:id_estimate>', methods=['POST'])
@cross_origin()
def calculate_estimate(id_estimate):
    # Принимаем json { client_fio, use_base, project_id
    # additional_works: [1, 2, ...] (optional),
    # work_technologies: [1, 2, ...] (optional) }
    api.estimate.EstimateImpl.calculate_estimate(id_estimate, request.json)
    return jsonify('True')


@estimate_api.route(f'{api_version}/get_estimate_materials/<int:id_estimate>', methods=['GET'])
@cross_origin()
def get_estimate_materials(id_estimate):
    data = api.estimate.EstimateImpl.get_estimate_materials(id_estimate)
    return jsonify(data)


@estimate_api.route(f'{api_version}/get_estimate_works/<int:id_estimate>', methods=['GET'])
@cross_origin()
def get_estimate_works(id_estimate):
    data = api.estimate.EstimateImpl.get_estimate_works(id_estimate)
    return jsonify(data)


@estimate_api.route(f'{api_version}/export_estimate/<int:id_estimate>', methods=['GET'])
@cross_origin()
def export_estimate(id_estimate):
    api.estimate.EstimateImpl.export_estimate(id_estimate)
    return jsonify('True')


@estimate_api.route(f'{api_version}/get_project_technologies/<int:id_project>', methods=['GET'])
@cross_origin()
def get_project_technologies(id_project):
    data = api.estimate.EstimateImpl.get_project_technologies(id_project)
    return jsonify(data)
