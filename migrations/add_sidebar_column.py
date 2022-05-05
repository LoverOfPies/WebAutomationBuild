from peewee import BooleanField
from playhouse.migrate import SchemaMigrator, migrate

from api.app import db


def run_script():
    migrator = SchemaMigrator(db.database)
    try:
        migrate(migrator.add_column('ab_table_info', 'show_in_sidebar', BooleanField(verbose_name='Отображать в sidebar', default=False)))
        return True
    except:
        return False
