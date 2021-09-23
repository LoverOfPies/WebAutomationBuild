from peewee import CharField, ForeignKeyField, DoubleField

from app import db
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.work.WorkGroup import WorkGroup


# Работа
class Work(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    work_coefficient = DoubleField(default=0, verbose_name='Коэффициэнт')
    client_price = DoubleField(default=0, verbose_name='Тариф клиента')
    work_price = DoubleField(default=0, verbose_name='Тариф себестоимости')
    base_unit = ForeignKeyField(BaseUnit, backref='works', verbose_name='Базовая единица')
    work_group = ForeignKeyField(WorkGroup, backref='works', verbose_name='Группа работ')

    class Meta:
        db_table = "ab_work"
