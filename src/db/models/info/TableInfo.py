import peewee

from app import db


class TableInfo(db.Model):
    name = peewee.CharField(unique=True, verbose_name='Наименование таблицы')
    path = peewee.CharField(verbose_name='Путь к model')
    icon = peewee.CharField(verbose_name='Иконка')
    title = peewee.CharField(verbose_name='Русское наименование таблицы')
    readonly = peewee.BooleanField(verbose_name='Только для чтения')
    many_to_many = peewee.BooleanField(verbose_name='Таблица множественной связки')
    group_field = peewee.CharField(verbose_name='Поле группировки')

    class Meta:
        db_table = "ab_table_info"
