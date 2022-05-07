__version__ = '/api/v0.1'
__author__ = 'Ilya Antipov'

import sys
from uuid import uuid4

import peewee


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)


class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True, null=False)
    uuid = peewee.UUIDField(default=uuid4)

    class Meta:
        database = load_class('api.app.db').database
        order_by = 'id'
