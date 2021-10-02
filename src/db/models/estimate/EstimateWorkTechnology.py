from peewee import ForeignKeyField

from app import db
from src.db.models.estimate.Estimate import Estimate
from src.db.models.work.WorkTechnology import WorkTechnology


# ManyToMany Технологии работ для расчёта
class WorkGroupTechnology(db.Model):
    estimate = ForeignKeyField(Estimate, backref='estimates')
    work_technology = ForeignKeyField(WorkTechnology, backref='work_technologies')

    class Meta:
        db_table = "ab_technology_estimate"
