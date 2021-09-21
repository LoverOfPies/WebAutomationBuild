from peewee import ForeignKeyField, CharField, IntegerField

from app import db
from src.db.models.project.Project import Project
from src.db.models.provider.City import City


# Расчёт
class Estimate(db.Model):
    number = IntegerField(unique=True)
    client_fio = CharField(unique=True)
    city = ForeignKeyField(City, backref='estimates')
    project = ForeignKeyField(Project, backref='estimates')

    class Meta:
        db_table = "ab_estimate"
