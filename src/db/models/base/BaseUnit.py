from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.base.Unit import Unit


# Базовая единица
class BaseUnit(db.Model):
    name = CharField(unique=True)
    unit = ForeignKeyField(Unit, backref='units')

    class Meta:
        db_table = "ab_base_unit"
