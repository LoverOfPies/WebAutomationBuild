import json

from flask import Flask
from flask_cors import CORS

from src.db.Database import Database

app = Flask(__name__, static_url_path='')
CORS(app)

app.config.from_file("config.json", load=json.load)
app.config['CORS_HEADERS'] = 'Content-Type'

db = Database(app)
