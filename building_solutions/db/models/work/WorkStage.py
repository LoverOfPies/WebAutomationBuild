from peewee import CharField

from db import BaseModel


# Стадии работ
class WorkStage(BaseModel):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_work_stage"
