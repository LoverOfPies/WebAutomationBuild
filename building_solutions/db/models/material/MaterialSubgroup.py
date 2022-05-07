from peewee import CharField, ForeignKeyField

from db import BaseModel
from db.models.extender.ClsIdExtender import ClsIdExtender
from db.models.material.MaterialGroup import MaterialGroup


# Подгруппа
class MaterialSubgroup(BaseModel, ClsIdExtender):
    name = CharField(verbose_name='Наименование')
    material_group = ForeignKeyField(MaterialGroup, backref='material_subgroups', verbose_name='Группа материала')

    class Meta:
        db_table = "ab_material_subgroup"
