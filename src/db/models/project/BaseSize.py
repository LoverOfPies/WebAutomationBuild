from peewee import ForeignKeyField, DoubleField

from app import db
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.project.Project import Project


# Базовый размер
class BaseSize(db.Model):
    amount = DoubleField(verbose_name='Кол-во', default=0, null=True)
    project = ForeignKeyField(Project, backref='base_sizes', verbose_name='Проект')
    base_unit = ForeignKeyField(BaseUnit, backref='base_sizes', verbose_name='Базовая единица')

    class Meta:
        db_table = "ab_base_size"
