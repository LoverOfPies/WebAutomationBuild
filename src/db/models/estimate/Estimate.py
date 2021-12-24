from peewee import ForeignKeyField, CharField, IntegerField, BooleanField, DoubleField

from app import db
from src.db.models.project.Project import Project


# Расчёт
class Estimate(db.Model):
    number = IntegerField(unique=True, verbose_name='Номер', null=True)
    client_fio = CharField(verbose_name='ФИО клиента')
    use_base = BooleanField(verbose_name='Базовая комплектация', null=True)
    price_client = DoubleField(default=0, verbose_name='Цена заказчика', null=True)
    price_base = DoubleField(default=0, verbose_name='Цена базовая', null=True)
    project = ForeignKeyField(Project, backref='estimates', verbose_name='Проект', null=True)

    class Meta:
        db_table = "ab_estimate"
