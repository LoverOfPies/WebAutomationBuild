from openpyxl import load_workbook


def import_single_row(file, model_class):
    wb = load_workbook(file)
    sheet = wb.get_sheet_by_name('Лист1')
    values = []
    for cell in sheet['A']:
        if cell.row == 1:
            continue
        values.append([{'name': str(cell.value)}])
    data = dict([
        ('model_class', model_class),
        ('value', values),
    ])
