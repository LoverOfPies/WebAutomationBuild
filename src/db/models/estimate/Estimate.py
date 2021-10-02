from peewee import ForeignKeyField, CharField, IntegerField, BooleanField

from app import db
from src.db.models.project.Project import Project


# Расчёт
class Estimate(db.Model):
    number = IntegerField(unique=True, verbose_name='Номер')
    client_fio = CharField(verbose_name='ФИО клиента')
    use_base = BooleanField(verbose_name='Базовая комплектация')
    project = ForeignKeyField(Project, backref='estimates', verbose_name='Проект')

    class Meta:
        db_table = "ab_estimate"
