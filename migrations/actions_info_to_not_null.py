from playhouse.migrate import SchemaMigrator, migrate

from app import db


def run_script():
    # ALTER TABLE ab_action_info ALTER COLUMN to DROP NOT NULL
    migrator = SchemaMigrator(db.database)
    try:
        migrate(migrator.drop_not_null('ab_action_info', 'to'))
        return True
    except:
        return False
