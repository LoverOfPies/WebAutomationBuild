from peewee import ForeignKeyField

from db import BaseModel
from db.models.estimate.Estimate import Estimate
from db.models.work.Work import Work


# ManyToMany Технологии работ для расчёта
class EstimateAdditionalWork(BaseModel):
    estimate = ForeignKeyField(Estimate, backref='estimates')
    work = ForeignKeyField(Work, backref='works')

    class Meta:
        db_table = "ab_estimate_additional"
