from peewee import ForeignKeyField, DoubleField

from app import db
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.project.Project import Project


# Базовый объём
class BaseVolume(db.Model):
    amount = DoubleField(unique=True, verbose_name='Наименование')
    project = ForeignKeyField(Project, backref='base_volumes', verbose_name='Проект')
    base_unit = ForeignKeyField(BaseUnit, backref='base_volumes', verbose_name='Базовая единица')

    class Meta:
        db_table = "ab_base_volume"
