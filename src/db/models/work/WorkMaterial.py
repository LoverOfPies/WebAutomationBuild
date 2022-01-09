from peewee import DoubleField, ForeignKeyField

from app import db
from src.db.models.material.Material import Material
from src.db.models.work.Work import Work


# Материал для работы
class WorkMaterial(db.Model):
    material_coefficient = DoubleField(default=1, verbose_name='Коэффициэнт', null=True)
    amount = DoubleField(default=0, verbose_name='Количество используемого материала на единицу измерения')
    material = ForeignKeyField(Material, backref='work_materials', verbose_name='Материал')
    work = ForeignKeyField(Work, backref='work_materials', verbose_name='Работа')

    class Meta:
        db_table = "ab_work_material"
