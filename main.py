from api import *
from src.ApiUtils import init_base

if __name__ == '__main__':
    init_base()
    app.run(port=1337)
