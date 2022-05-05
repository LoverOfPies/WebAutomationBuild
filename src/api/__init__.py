__version__ = '/api/v0.1'
__author__ = 'Ilya Antipov'

import sys


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)
