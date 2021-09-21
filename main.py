import inspect
import sys

from app import app, db
from api import *
from src.db.models import *

if __name__ == '__main__':
    app.run()
