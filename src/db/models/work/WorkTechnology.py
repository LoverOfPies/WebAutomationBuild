from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.work.WorkStage import WorkStage


# Технология работ
class WorkTechnology(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    work_stage = ForeignKeyField(WorkStage, backref='work_technologies', verbose_name='Этап работ')

    class Meta:
        db_table = "ab_work_technology"
