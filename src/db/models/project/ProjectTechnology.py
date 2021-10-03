from peewee import ForeignKeyField

from app import db
from src.db.models.project.Project import Project
from src.db.models.work.WorkTechnology import WorkTechnology


# ManyToMany Технологии для проекта
class ProjectTechnology(db.Model):
    project = ForeignKeyField(Project, backref='projects', verbose_name='Проект')
    work_technology = ForeignKeyField(WorkTechnology, backref='work_technologies', verbose_name='Технология')

    class Meta:
        db_table = "ab_project_technology"
