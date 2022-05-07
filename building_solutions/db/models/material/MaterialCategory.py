from peewee import CharField

from db import BaseModel
from db.models.extender.ClsIdExtender import ClsIdExtender


# Категория
class MaterialCategory(BaseModel, ClsIdExtender):
    name = CharField(verbose_name='Наименование')

    class Meta:
        db_table = "ab_material_category"
