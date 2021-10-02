from peewee import CharField, ForeignKeyField

from app import db


# Группа работ
class WorkGroup(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_work_group"
