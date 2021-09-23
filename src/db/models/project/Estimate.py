from peewee import ForeignKeyField, CharField, IntegerField

from app import db
from src.db.models.project.Project import Project
from src.db.models.provider.City import City


# Расчёт
class Estimate(db.Model):
    number = IntegerField(unique=True, verbose_name='Номер')
    client_fio = CharField(unique=True, verbose_name='ФИО клиента')
    city = ForeignKeyField(City, backref='estimates', verbose_name='Город')
    project = ForeignKeyField(Project, backref='estimates', verbose_name='Проект')

    class Meta:
        db_table = "ab_estimate"
