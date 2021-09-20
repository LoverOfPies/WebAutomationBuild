import json

from flask import Flask, render_template, request, redirect
from flask_peewee.db import Database
from flask_peewee.utils import object_list

from src.db.models.provider.City import City

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)
db = Database(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test/<string:name>/<int:value_id>')
def test(name, value_id):
    return f'Test!: {name}, {value_id}'


@app.route('/create_table', methods=['POST', 'GET'])
def create_table():
    if request.method == 'POST':
        title = request.form['title']
        print(title)
        return redirect('/')
    else:
        return render_template('create_table.html')


@app.route('/city')
def city():
    cities = City.select().order_by(City.name)
    return object_list('city.html', cities, 'city_list')
