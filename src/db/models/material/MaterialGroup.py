from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.material.MaterialCategory import MaterialCategory


# Группа
class MaterialGroup(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    material_category = ForeignKeyField(MaterialCategory, backref='material_groups', verbose_name='Категория материала')

    class Meta:
        db_table = "ab_material_group"
