from peewee import ForeignKeyField

from app import db
from src.db.models.project.Equipment import Equipment
from src.db.models.project.Project import Project


# ManyToMany Комплектации для проекта
class ProjectEquipment(db.Model):
    project = ForeignKeyField(Project, backref='equipments')
    equipment = ForeignKeyField(Equipment, backref='projects')

    class Meta:
        db_table = "ab_project_equipment"
