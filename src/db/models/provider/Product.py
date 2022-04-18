from peewee import ForeignKeyField, DoubleField

from app import db
from src.db.models.extender.VersioningExtender import VersioningExtender
from src.db.models.material.Material import Material
from src.db.models.provider.Provider import Provider


# Товар
class Product(db.Model, VersioningExtender):
    amount_for_one = DoubleField(default=0, verbose_name='Объём материала в упаковке')
    material = ForeignKeyField(Material, backref='products', verbose_name='Материал')
    price = DoubleField(default=0, verbose_name='Цена за упаковку')

    class Meta:
        db_table = "ab_product"
