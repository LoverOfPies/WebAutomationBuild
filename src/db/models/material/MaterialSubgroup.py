from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.material.MaterialGroup import MaterialGroup


# Подгруппа
class MaterialSubgroup(db.Model):
    name = CharField(unique=True)
    material_group = ForeignKeyField(MaterialGroup, backref='material_subgroups')

    class Meta:
        db_table = "ab_material_subgroup"
