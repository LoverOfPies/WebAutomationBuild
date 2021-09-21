import json

from flask import Flask

from src.db.Database import Database

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)
db = Database(app)
