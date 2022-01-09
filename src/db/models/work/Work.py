from peewee import CharField, ForeignKeyField, DoubleField, BooleanField

from app import db
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.work.WorkGroup import WorkGroup


# Работа
class Work(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    fix_price = BooleanField(default=False, verbose_name='Фиксированная цена', null=True)
    client_price = DoubleField(default=0, verbose_name='Тариф клиента', null=True)
    work_price = DoubleField(default=0, verbose_name='Тариф себестоимости', null=True)
    work_base = BooleanField(verbose_name='Базовая работа', null=True)
    base_unit = ForeignKeyField(BaseUnit, backref='works', verbose_name='Базовая единица')
    work_group = ForeignKeyField(WorkGroup, backref='works', verbose_name='Группа работ')

    class Meta:
        db_table = "ab_work"
