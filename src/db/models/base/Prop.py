from peewee import CharField

from app import db


# Свойства для материалов (длина, ширина и т.д.)
class Prop(db.Model):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_property"
