from peewee import CharField, ForeignKeyField

from db import BaseModel
from db.models.work.WorkStage import WorkStage


# Технология работ
class WorkTechnology(BaseModel):
    name = CharField(unique=True, verbose_name='Наименование')
    work_stage = ForeignKeyField(WorkStage, backref='work_technologies', verbose_name='Стадия работ')

    class Meta:
        db_table = "ab_work_technology"
