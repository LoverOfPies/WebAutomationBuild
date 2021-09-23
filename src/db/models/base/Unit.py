from peewee import CharField

from app import db


# Единица измерения (метры, сантиметры, шт., кубы и т.д.)
class Unit(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_unit"
