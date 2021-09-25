from openpyxl import load_workbook


def import_single_row(model, file_name):
    wb = load_workbook(file_name)
    sheet = wb.get_sheet_by_name('Лист1')
    values = []
    for cell in sheet['A']:
        if cell.row == 1:
            continue
        values.append([{'name': str(cell.value)}])
