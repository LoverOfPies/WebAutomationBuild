from peewee import CharField, ForeignKeyField


from app import db
from src.db.models.extender.ClsIdExtender import ClsIdExtender
from src.db.models.material.MaterialSubgroup import MaterialSubgroup
from src.db.models.base.Unit import Unit


# Материал
class Material(db.Model):
    name = CharField(verbose_name='Наименование')
    articul = CharField(verbose_name='Артикул', null=True)
    unit = ForeignKeyField(Unit, backref='materials', verbose_name='Единицы измерения')
    material_subgroup = ForeignKeyField(MaterialSubgroup, backref='materials', verbose_name='Подгруппа')

    class Meta:
        db_table = "ab_material"
