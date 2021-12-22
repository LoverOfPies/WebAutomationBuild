from peewee import ForeignKeyField

from app import db
from src.db.models.estimate.Estimate import Estimate
from src.db.models.work.Work import Work


# ManyToMany Технологии работ для расчёта
class EstimateAdditionalWork(db.Model):
    estimate = ForeignKeyField(Estimate, backref='estimates')
    work = ForeignKeyField(Work, backref='works')

    class Meta:
        db_table = "ab_additional_estimate"
