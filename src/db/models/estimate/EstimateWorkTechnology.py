from peewee import ForeignKeyField

from db import BaseModel
from db.models.estimate.Estimate import Estimate
from db.models.work.WorkTechnology import WorkTechnology


# ManyToMany Технологии работ для расчёта
class EstimateWorkTechnology(BaseModel):
    estimate = ForeignKeyField(Estimate, backref='estimates')
    work_technology = ForeignKeyField(WorkTechnology, backref='work_technologies')

    class Meta:
        db_table = "ab_estimate_technology"
