from peewee import CharField

from db import BaseModel


# Свойства для материалов (длина, ширина и т.д.)
class Prop(BaseModel):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_property"
