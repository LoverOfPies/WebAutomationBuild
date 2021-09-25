from openpyxl import load_workbook


def import_single_row(model, file_name):
    wb = load_workbook(file_name)
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
