from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.base.Unit import Unit


# Базовая единица
class BaseUnit(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    unit = ForeignKeyField(Unit, backref='units', verbose_name='Единица измерения')

    class Meta:
        db_table = "ab_base_unit"
