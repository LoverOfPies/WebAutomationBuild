import inspect
import sys

from app import app, db
from api import *
from src.db.models import *
from src.expimp import *
from src.utils import init_base

if __name__ == '__main__':
    # init_base()
    app.run()
