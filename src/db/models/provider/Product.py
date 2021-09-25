from peewee import ForeignKeyField, DoubleField

from app import db
from src.db.models.extender.VersioningExtender import VersioningExtender
from src.db.models.material.Material import Material
from src.db.models.provider.Provider import Provider


# Товар
class Product(db.Model, VersioningExtender):
    price = DoubleField(default=0, verbose_name='Цена')
    amount_for_one = DoubleField(default=0, verbose_name='Количество материала за 1 шт')
    provider = ForeignKeyField(Provider, backref='products', verbose_name='Поставщик')
    material = ForeignKeyField(Material, backref='products', verbose_name='Материал')

    class Meta:
        db_table = "ab_product"
