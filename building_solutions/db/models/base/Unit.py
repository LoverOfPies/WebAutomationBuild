from peewee import CharField

from db import BaseModel


# Единица измерения (метры, сантиметры, шт., кубы и т.д.)
class Unit(BaseModel):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_unit"
