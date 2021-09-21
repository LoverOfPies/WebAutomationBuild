from peewee import CharField

from app import db


# Категория
class MaterialCategory(db.Model):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_material_category"
