from peewee import ForeignKeyField, DoubleField

from db import BaseModel
from db.models.extender.VersioningExtender import VersioningExtender
from db.models.material.Material import Material


# Товар
class Product(BaseModel, VersioningExtender):
    amount_for_one = DoubleField(default=0, verbose_name='Объём материала в упаковке')
    material = ForeignKeyField(Material, backref='products', verbose_name='Материал')
    price = DoubleField(default=0, verbose_name='Цена за упаковку')

    class Meta:
        db_table = "ab_product"
