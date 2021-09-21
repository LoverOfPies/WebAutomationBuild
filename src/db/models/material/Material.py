from peewee import CharField, ForeignKeyField


from app import db
from src.db.models.material.MaterialSubgroup import MaterialSubgroup
from src.db.models.base.Unit import Unit


# Материал
class Material(db.Model):
    name = CharField(unique=True)                           # наименование
    articul = CharField()                                   # артикул
    unit = ForeignKeyField(Unit, backref='materials')       # единицы измерения (шт, кубы и т.д.)
    subgroup = ForeignKeyField(MaterialSubgroup, backref='materials')  # подгруппа

    class Meta:
        db_table = "ab_material"
