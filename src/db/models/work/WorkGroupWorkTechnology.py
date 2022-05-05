from peewee import ForeignKeyField

from db import BaseModel
from db.models.work.WorkTechnology import WorkTechnology
from db.models.work.WorkGroup import WorkGroup


# ManyToMany Группы работ для данной технологии
class WorkGroupWorkTechnology(BaseModel):
    work_group = ForeignKeyField(WorkGroup, backref='work_groups', verbose_name='Группа работ')
    work_technology = ForeignKeyField(WorkTechnology, backref='work_technologies', verbose_name='Технология')

    class Meta:
        db_table = "ab_technology_group"
