from peewee import ForeignKeyField, DoubleField

from db import BaseModel
from src.db.models.base.BaseUnit import BaseUnit
from src.db.models.estimate.Estimate import Estimate


# Базовый размер
class EstimateBaseSize(BaseModel):
    amount = DoubleField(verbose_name='Кол-во', default=0, null=True)
    estimate = ForeignKeyField(Estimate, backref='estimate_base_sizes', verbose_name='Расчёт')
    base_unit = ForeignKeyField(BaseUnit, backref='estimate_base_sizes', verbose_name='Базовая единица')

    class Meta:
        db_table = "ab_estimate_base_size"
