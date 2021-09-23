from peewee import DoubleField, ForeignKeyField

from app import db
from src.db.models.material.Material import Material
from src.db.models.base.Prop import Prop
from src.db.models.base.Unit import Unit


# Свойство и параметры для конкретного материала
class MaterialProperty(db.Model):
    amount = DoubleField(default=0, verbose_name='Число')
    material = ForeignKeyField(Material, backref='material_properties', verbose_name='Материал')
    prop = ForeignKeyField(Prop, backref='material_properties', verbose_name='Свойство')
    unit = ForeignKeyField(Unit, backref='material_properties', verbose_name='Единица измерения')

    class Meta:
        db_table = "ab_material_property"
