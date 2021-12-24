from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.work.WorkStage import WorkStage


# Группа работ
class WorkGroup(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    work_stage = ForeignKeyField(WorkStage, backref='work_groups', verbose_name='Стадия работ')

    class Meta:
        db_table = "ab_work_group"
