import peewee

from db import BaseModel
from db.models.info.TableInfo import TableInfo


class ActionInfo(BaseModel):
    action = peewee.CharField(verbose_name='Действие на клиенте (route)')
    label = peewee.CharField(verbose_name='Наименование')
    to = peewee.CharField(verbose_name='Если route, то экран для перехода', null=True)
    table = peewee.ForeignKeyField(TableInfo, backref='actions', verbose_name='Таблица для которой действие')

    class Meta:
        db_table = "ab_action_info"
