from peewee import BooleanField, SQL
from playhouse.migrate import SchemaMigrator, migrate

from api.app import db


def run_script():
    migrator = SchemaMigrator(db.database)
    try:
        SQL('ALTER TABLE ab_work ALTER work_base SET DEFAULT False;')
        return True
    except:
        return False