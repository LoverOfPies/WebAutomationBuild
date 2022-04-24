from src.db.DataBaseUtils import get_record, get_or_insert
from src.db.models.info.ActionInfo import ActionInfo
from src.db.models.info.TableInfo import TableInfo


def run_script():
    product_table = get_record(TableInfo, {'name': 'product'})
    obj = get_or_insert(ActionInfo, {'action': 'versioning', 'label': 'Журнал изменений', 'table': product_table.id})
    return bool(obj)
