from peewee import ForeignKeyField, DoubleField, IntegerField

from db import BaseModel
from db.models.estimate.Estimate import Estimate
from db.models.provider.Product import Product


# Материалы для расчёта
class EstimateMaterial(BaseModel):
    estimate = ForeignKeyField(Estimate, backref='estimates')
    amount = IntegerField(verbose_name='Количество упаковок', null=True)
    product = ForeignKeyField(Product, backref='products')
    price = DoubleField(default=0, verbose_name='Цена', null=True)

    class Meta:
        db_table = "ab_estimate_material"
