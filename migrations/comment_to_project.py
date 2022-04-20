from peewee import CharField
from playhouse.migrate import SchemaMigrator, migrate

from app import db


def run_script():
    migrator = SchemaMigrator(db.database)
    try:
        migrate(migrator.add_column('ab_project', 'comment', CharField(verbose_name='Комментарий', null=True)))
        return True
    except:
        return False
