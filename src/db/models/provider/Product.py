from peewee import ForeignKeyField, DoubleField, DateField

from app import db
from src.db.models.material.Material import Material
from src.db.models.provider.Provider import Provider


# Товар
class Product(db.Model):
    price = DoubleField(default=0)                              # цена
    amount_for_one = DoubleField(default=0)                     # количество материала за 1 шт
    provider = ForeignKeyField(Provider, backref='products')    # поставщик
    material = ForeignKeyField(Material, backref='products')    # материал
    date_load = DateField()                                     # дата выгрузки товаров

    class Meta:
        db_table = "ab_product"
