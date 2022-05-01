from peewee import BooleanField, DateField
from playhouse.migrate import SchemaMigrator, migrate

from app import db


def run_script():
    migrator = SchemaMigrator(db.database)
    try:
        migrate(migrator.add_column('ab_estimate', 'active',
                                    BooleanField(verbose_name='Признак активности', null=True)),
                migrator.add_column('ab_estimate', 'create_date',
                                    DateField(verbose_name='Дата создания', null=True)),
                migrate(migrator.drop_not_null('ab_estimate', 'client_fio')))
        return True
    except:
        return False
