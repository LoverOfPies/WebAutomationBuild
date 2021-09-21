from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.provider.City import City


# Поставщик
class Provider(db.Model):
    name = CharField(unique=True)
    city = ForeignKeyField(City, backref='providers')

    class Meta:
        db_table = "ab_provider"
