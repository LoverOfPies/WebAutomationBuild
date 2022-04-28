from app import app
from src.db import DataBaseUtils

if __name__ == '__main__':
    # DataBaseUtils.init_base()
    app.run(host='0.0.0.0', port=1337)
