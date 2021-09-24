import peewee

from app import db
from src.db.models.info.TableInfo import TableInfo


class FilterInfo(db.Model):
    key = peewee.CharField(verbose_name='Таблица фильтра')
    label = peewee.CharField(verbose_name='Наименование')
    multiple = peewee.CharField(verbose_name='Наименование во множественном числе')
    table = peewee.ForeignKeyField(TableInfo, backref='filters', verbose_name='Таблица для которой фильтр')

    class Meta:
        db_table = "ab_filter_info"
