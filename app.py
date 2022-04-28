import json

from flask import Flask, send_from_directory, make_response, jsonify
from flask_cors import CORS

from MyAppException import MyAppException
from src.db.Database import Database
from src.api.estimate import estimate_api
from src.api.base import base_api

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

app.config.from_file("config.json", load=json.load)
app.register_blueprint(estimate_api)
app.register_blueprint(base_api)

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
