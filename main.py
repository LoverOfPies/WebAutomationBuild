from api import *
from src.db import DataBaseUtils

if __name__ == '__main__':
    DataBaseUtils.init_base()
    app.run(port=1337)
