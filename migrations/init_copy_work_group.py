from src.db.DataBaseUtils import insert_record, get_record
from src.db.models.info.ActionInfo import ActionInfo
from src.db.models.info.TableInfo import TableInfo


def run_script():
    work_group_table = get_record(TableInfo, {'name': 'work_group'})
    obj = insert_record(ActionInfo, {'action': 'copy', 'label': 'Копировать группу', 'table': work_group_table.id})
    return bool(obj)
