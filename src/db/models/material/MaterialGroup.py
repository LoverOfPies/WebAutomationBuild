from peewee import CharField, ForeignKeyField

from db import BaseModel
from db.models.extender.ClsIdExtender import ClsIdExtender
from db.models.material.MaterialCategory import MaterialCategory


# Группа
class MaterialGroup(BaseModel, ClsIdExtender):
    name = CharField(verbose_name='Наименование')
    material_category = ForeignKeyField(MaterialCategory, backref='material_groups', verbose_name='Категория материала')

    class Meta:
        db_table = "ab_material_group"
