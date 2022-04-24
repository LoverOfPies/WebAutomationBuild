from peewee import BooleanField
from playhouse.migrate import SchemaMigrator, migrate

from app import db


def run_script():
    migrator = SchemaMigrator(db.database)
    try:
        migrate(migrator.add_column('ab_product', 'enable_version',
                                    BooleanField(verbose_name='Действующая версия', default=True)))
        return True
    except:
        return False
