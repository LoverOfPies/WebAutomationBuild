import json

from flask import Flask, send_from_directory, make_response, jsonify
from flask_cors import CORS

from api.base.MyAppException import MyAppException
from api.base.Database import Database
from api.estimate import estimate_api
from api.base import base_api
from api.history import history_api

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

app.config.from_file("config.json", load=json.load)
app.register_blueprint(estimate_api)
app.register_blueprint(base_api)
app.register_blueprint(history_api)

db = Database(app)


@app.route('/', defaults={'path': ''})
@app.route('/dict/<path:path>')
@app.route('/settings')
def index(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(MyAppException)
def http_error_handler(error):
    return make_response(jsonify({'error': error.message}), 500)
