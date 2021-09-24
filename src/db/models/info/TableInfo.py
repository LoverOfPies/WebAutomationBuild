import peewee

from app import db


class TableInfo(db.Model):
    name = peewee.CharField(unique=True, verbose_name='Наименование таблицы')
    path = peewee.CharField(verbose_name='Путь к model')
    icon = peewee.CharField(verbose_name='Иконка')
    title = peewee.CharField(verbose_name='Русское наименование таблицы')

    class Meta:
        db_table = "ab_table_info"
