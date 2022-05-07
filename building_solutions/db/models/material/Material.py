from peewee import CharField, ForeignKeyField


from db import BaseModel
from db.models.material.MaterialSubgroup import MaterialSubgroup
from db.models.base.Unit import Unit


# Материал
class Material(BaseModel):
    name = CharField(verbose_name='Наименование')
    articul = CharField(verbose_name='Артикул', null=True)
    unit = ForeignKeyField(Unit, backref='materials', verbose_name='Единицы измерения')
    material_subgroup = ForeignKeyField(MaterialSubgroup, backref='materials', verbose_name='Подгруппа')

    class Meta:
        db_table = "ab_material"
