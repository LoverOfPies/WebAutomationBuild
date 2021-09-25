from openpyxl import load_workbook

from src.utils import get_file_name


def import_single_table(model, file_path):
    wb = load_workbook(file_path)
    sheet = wb.active
    fields = {}
    data = []
    for row in sheet:
        value = {}
        for cell in row:
            if cell.row == 1:
                if not hasattr(model, cell.value):
                    return False
                fields[cell.column] = cell.value
                continue
            value[fields[cell.column]] = cell.value
        if len(value) > 0:
            data.append(value)
    model.insert(data).execute()
    return True


def import_custom_data(file_path):
    file_name = get_file_name(file_path)
    if file_name.lower() == 'Материалы'.lower():
        import_material_table(file_path)
        return True
    return False


def import_material_table(file_path):
    wb = load_workbook(file_path)
    sheet = wb.active
    for row in sheet:
        for cell in row:
            print(cell)
