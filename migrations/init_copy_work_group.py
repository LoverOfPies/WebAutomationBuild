from src.db.DataBaseUtils import get_record, get_or_insert
from src.db.models.info.ActionInfo import ActionInfo
from src.db.models.info.TableInfo import TableInfo


def run_script():
    work_group_table = get_record(TableInfo, {'name': 'work_group'})
    obj = get_or_insert(ActionInfo, {'action': 'copy', 'label': 'Копировать группу', 'table': work_group_table.id})
    return bool(obj)
