from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.extender.ClsIdExtender import ClsIdExtender
from src.db.models.material.MaterialGroup import MaterialGroup


# Подгруппа
class MaterialSubgroup(db.Model, ClsIdExtender):
    name = CharField(unique=True, verbose_name='Наименование')
    material_group = ForeignKeyField(MaterialGroup, backref='material_subgroups', verbose_name='Группа материала')

    class Meta:
        db_table = "ab_material_subgroup"
