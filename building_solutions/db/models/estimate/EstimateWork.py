from peewee import ForeignKeyField, DoubleField

from db import BaseModel
from db.models.estimate.Estimate import Estimate
from db.models.work.Work import Work


# Работа для расчёта
class EstimateWork(BaseModel):
    estimate = ForeignKeyField(Estimate, backref='estimates')
    work = ForeignKeyField(Work, backref='works')
    client_price = DoubleField(default=0, verbose_name='Цена работы клиента', null=True)
    base_price = DoubleField(default=0, verbose_name='Цена себестоимости', null=True)

    class Meta:
        db_table = "ab_estimate_work"
