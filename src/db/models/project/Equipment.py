from peewee import CharField

from app import db


# Комплектация
class Equipment(db.Model):
    name = CharField(unique=True)

    class Meta:
        db_table = "ab_equipment"
