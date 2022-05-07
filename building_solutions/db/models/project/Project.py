from peewee import CharField

from db import BaseModel


# Проект
class Project(BaseModel):
    name = CharField(unique=True, verbose_name='Наименование')
    comment = CharField(verbose_name='Комментарий', null=True)

    class Meta:
        db_table = "ab_project"
