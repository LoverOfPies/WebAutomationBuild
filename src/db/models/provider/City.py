from peewee import CharField
from app import db


# Город
class City(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_city"
