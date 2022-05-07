from peewee import CharField, ForeignKeyField

from db import BaseModel
from db.models.base.Unit import Unit


# Базовая единица
class BaseUnit(BaseModel):
    name = CharField(unique=True, verbose_name='Наименование')
    unit = ForeignKeyField(Unit, backref='units', verbose_name='Единица измерения')

    class Meta:
        db_table = "ab_base_unit"
