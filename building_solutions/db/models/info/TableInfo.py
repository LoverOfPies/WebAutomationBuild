import peewee

from db import BaseModel


class TableInfo(BaseModel):
    name = peewee.CharField(unique=True, verbose_name='Наименование таблицы')
    path = peewee.CharField(verbose_name='Путь к model')
    icon = peewee.CharField(verbose_name='Иконка', null=True)
    title = peewee.CharField(verbose_name='Русское наименование таблицы', null=True)
    readonly = peewee.BooleanField(verbose_name='Только для чтения', null=True)
    many_to_many = peewee.BooleanField(verbose_name='Таблица множественной связки', null=True)
    group_field = peewee.CharField(verbose_name='Поле группировки', null=True)
    show_in_sidebar = peewee.BooleanField(verbose_name='Отображать в sidebar', default=False)

    class Meta:
        db_table = "ab_table_info"
