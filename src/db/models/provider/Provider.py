from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.provider.City import City


# Поставщик
class Provider(db.Model):
    name = CharField(verbose_name='Наименование')
    city = ForeignKeyField(City, backref='providers', verbose_name='Город')

    class Meta:
        db_table = "ab_provider"
