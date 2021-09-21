from peewee import CharField, ForeignKeyField, DoubleField

from app import db
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.work.WorkGroup import WorkGroup


# Работа
class Work(db.Model):
    name = CharField(unique=True)
    work_coefficient = DoubleField(default=0)                   # коэффицент для работы
    client_price = DoubleField(default=0)                       # тариф клиента
    work_price = DoubleField(default=0)                         # тариф себестоимости
    base_unit = ForeignKeyField(BaseUnit, backref='works')      # базовая единица
    work_group = ForeignKeyField(WorkGroup, backref='works')    # группа работ

    class Meta:
        db_table = "ab_work"
