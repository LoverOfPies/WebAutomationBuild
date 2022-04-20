from peewee import CharField

from app import db


# Проект
class Project(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')
    comment = CharField(verbose_name='Комментарий', null=True)

    class Meta:
        db_table = "ab_project"
