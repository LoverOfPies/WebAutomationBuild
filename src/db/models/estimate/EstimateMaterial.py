from peewee import ForeignKeyField, DoubleField

from app import db
from src.db.models.estimate.Estimate import Estimate
from src.db.models.provider.Product import Product


# Материалы для расчёта
class EstimateMaterial(db.Model):
    estimate = ForeignKeyField(Estimate, backref='estimates')
    product = ForeignKeyField(Product, backref='products')
    price = DoubleField(default=0, verbose_name='Цена', null=True)

    class Meta:
        db_table = "ab_estimate_material"
