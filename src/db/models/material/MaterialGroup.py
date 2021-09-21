from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.material.MaterialCategory import MaterialCategory


# Группа
class MaterialGroup(db.Model):
    name = CharField(unique=True)
    material_category = ForeignKeyField(MaterialCategory, backref='material_groups')

    class Meta:
        db_table = "ab_material_group"
