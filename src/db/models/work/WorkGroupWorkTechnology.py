from peewee import ForeignKeyField

from app import db
from src.db.models.work.WorkTechnology import WorkTechnology
from src.db.models.work.WorkGroup import WorkGroup


# ManyToMany Группы работ для данной технологии
class WorkGroupWorkTechnology(db.Model):
    work_group = ForeignKeyField(WorkGroup, backref='work_groups', verbose_name='Группа работ')
    work_technology = ForeignKeyField(WorkTechnology, backref='work_technologies', verbose_name='Технология')

    class Meta:
        db_table = "ab_technology_group"
