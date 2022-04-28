from uuid import uuid4
import os

import peewee
from peewee import ImproperlyConfigured
from playhouse.db_url import connect

from src.Cache import load_class


class Database(object):
    def __init__(self, app, database=None):
        self.app = app
        self.database = database

        if self.database is None:
            self.load_database()

        self.Model = self.get_model_class()

    def load_database(self):
        database_config = dict(self.app.config['DATABASE'])
        try:
            database_name = database_config.pop('name')
            database_engine = database_config.pop('engine')
        except KeyError:
            raise ImproperlyConfigured('Please specify a "name" and "engine" for your database')
        try:
            database_class = load_class(database_engine)
            assert issubclass(database_class, peewee.Database)
        except ImportError:
            raise ImproperlyConfigured('Unable to import: "%s"' % database_engine)
        except AttributeError:
            raise ImproperlyConfigured('Database engine not found: "%s"' % database_engine)
        except AssertionError:
            raise ImproperlyConfigured('Database engine not a subclass of peewee.Database: "%s"' % database_engine)

        if os.environ.get("IS_CONTAINER"):
            self.database = connect(os.environ.get("POSTGRES_URL"))
        else:
            self.database = database_class(database_name, **database_config)

    def get_model_class(self):
        class BaseModel(peewee.Model):
            id = peewee.PrimaryKeyField(unique=True, null=False)
            uuid = peewee.UUIDField(default=uuid4)

            class Meta:
                database = self.database
                order_by = 'id'
        return BaseModel
