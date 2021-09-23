from peewee import CharField, ForeignKeyField

from app import db
from src.db.models.work.WorkTechnology import WorkTechnology


# Группа работ
class WorkGroup(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    work_technology = ForeignKeyField(WorkTechnology, backref='work_groups', verbose_name='Технология работ')

    class Meta:
        db_table = "ab_work_group"
