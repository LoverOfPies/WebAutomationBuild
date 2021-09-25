from peewee import CharField

from app import db
from src.db.models.extender.ClsIdExtender import ClsIdExtender


# Категория
class MaterialCategory(db.Model, ClsIdExtender):
    name = CharField(verbose_name='Наименование')

    class Meta:
        db_table = "ab_material_category"
