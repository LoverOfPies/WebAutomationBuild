from flask import jsonify, request, Blueprint
from flask_cors import cross_origin
from werkzeug.exceptions import abort


from api import __version__ as api_version
from api.expimp import ExportImportUtils
import api.base.ApiImpl

base_api = Blueprint('base_api', __name__)


@base_api.route(f'{api_version}/get/<string:collection>', methods=['GET'])
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
    data = api.base.ApiImpl.get_data_from_table(collection, request.args)
    return jsonify(data)


@base_api.route(f'{api_version}/add/<string:collection>', methods=['POST'])
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
    result = api.base.ApiImpl.add_row(collection, request.json)
    if result:
        # TODO: Костыль [0]
        data = [row for row in result.dicts()][0]
        return jsonify(data)
    return abort(404)


@base_api.route(f'{api_version}/update/<string:collection>/<int:id_row>', methods=['PUT'])
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
    result = api.base.ApiImpl.update_row(collection, id_row, request.json)
    if result:
        return jsonify({'result': True})
    return abort(404)


@base_api.route(f'{api_version}/delete/<string:collection>/<int:id_row>', methods=['DELETE'])
@cross_origin()
def delete_value(collection, id_row):
    """
    Delete record from a table by id

    :param collection: table name
    :param id_row: record id

    :return: json
    """
    api.base.ApiImpl.delete_row(collection, id_row)
    return jsonify({'result': True})


# TODO: разбить на несколько методов
# К примеру, если у таблицы есть фильтры, отдавать признак
# После чего уже запрашивать фильтры
# С действиями возможно так же
@base_api.route(f'{api_version}/get_dict/<string:collection>', methods=['GET'])
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
    data = api.base.ApiImpl.get_dict_info(collection, request.args)
    return jsonify(data)


@base_api.route(f'{api_version}/get_dict', methods=['GET'])
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
    data = api.base.ApiImpl.get_dicts_info()
    return jsonify(data)


@base_api.route(f'{api_version}/sidebar', methods=['GET'])
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
    sidebar = api.base.ApiImpl.create_sidebar()
    return jsonify(sidebar)


@base_api.route(f'{api_version}/import/<string:collection>', methods=['POST'])
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


@base_api.route(f'{api_version}/export/<string:collection>', methods=['GET'])
@cross_origin()
def file_export(collection):
    ExportImportUtils.export_table(collection)
    return jsonify('True')


@base_api.route(f'{api_version}/copy_work_group/<int:id_work_group>', methods=['GET'])
@cross_origin()
def copy_work_group(id_work_group):
    new_work_group = api.base.ApiImpl.copy_work_group(id_work_group)
    return jsonify(new_work_group)
