from peewee import CharField, ForeignKeyField

from db import BaseModel
from db.models.provider.City import City


# Поставщик
class Provider(BaseModel):
    name = CharField(verbose_name='Наименование')
    city = ForeignKeyField(City, backref='providers', verbose_name='Город')

    class Meta:
        db_table = "ab_provider"
