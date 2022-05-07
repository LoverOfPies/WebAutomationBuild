from peewee import CharField
from db import BaseModel


# Город
class City(BaseModel):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_city"
