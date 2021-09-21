from peewee import ForeignKeyField

from app import db
from src.db.models.project.Equipment import Equipment
from src.db.models.work.WorkGroup import WorkGroup


# ManyToMany Группы работ для данной комплектации
class WorkGroupEquipment(db.Model):
    work_group = ForeignKeyField(WorkGroup, backref='equipments')
    equipment = ForeignKeyField(Equipment, backref='work_groups')

    class Meta:
        db_table = "ab_technology_equipment"
