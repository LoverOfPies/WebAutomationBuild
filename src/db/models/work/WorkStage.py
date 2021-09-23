from peewee import CharField

from app import db


# Этап работ
class WorkStage(db.Model):
    name = CharField(unique=True, verbose_name='Наименование')

    class Meta:
        db_table = "ab_work_stage"
