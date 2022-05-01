from openpyxl import Workbook
from dataclasses import dataclass
from src.api.base.ApiImpl import get_data_from_table
import pprint

@dataclass
class EstimateWorkGroup:
    stage_name: str
    technology_name: str
    group_name: str
    work_list: list

pp = pprint.PrettyPrinter(indent=2)
print = lambda x: pp.pprint(x)

# test data
ESTIMATE_NAME = "estimate_export"
ESTIMATE_TABLE = "estimate"
ESTIMATE_ID = 1
DIST_FILENAME = f"{ESTIMATE_NAME}.xlsx"

# Базовые заголовки
BASE_HEADERS = (
    "База",
    "Тариф исполнитель",
    "Сумма исполнитель",
    "Тариф заказчик",
    "Сумма заказчик",
    "Кол-во/объем",
    "Ед.изм.",
    "Артикул",
    "Описание материала",
    "Материалы",
    "Ед.изм.",
    "Цена",
    "Кол-во/объем",
    "Сумма",
)

estimate_list = get_data_from_table("estimate", None)
# print(estimate_list)

estimate_info = get_data_from_table("estimate", {"id": ESTIMATE_ID})[0]

wb = Workbook()
ws = wb.active
ws.title = estimate_info["client_fio"]

for (index, header) in enumerate(BASE_HEADERS, start=6):
    ws[chr(ord('@')+index)+"1"] = header

# STAGES_INFO = get_data_from_table("work_stage")
# TECH_INFO = get_data_from_table("work_technology")
# GROUP_INFO = get_data_from_table("work_group", None)
# print(GROUP_INFO)

estimate_work_groups = []

# Используем базовые работы
if estimate_info["use_base"]:
    base_work_list = get_data_from_table("work", {"work_base": True})
    # print(base_work_list)
    for (index, base_work) in enumerate(base_work_list):
        # Собираем данные о группе работ
        wg_id = base_work["work_group"]
        work_group_info = get_data_from_table("work_group", {"id": wg_id})[0]
        # Собираем данные о группе технологий
        tech_groups_info = get_data_from_table("technology_group", {"work_group_id": work_group_info["id"]})
        tech_groups_list = []
        work_stages_list = []
        for tech_group in tech_groups_info:
            tg_id = tech_group["id"]
            tech_group_info = get_data_from_table("work_technology", {"id": tg_id})[0]
            tech_groups_list.append(tech_group_info["name"])
            print(tech_group_info)
            ws_id = tech_group_info["work_stage"]
            work_stage_info = get_data_from_table("work_stage", {"id": ws_id})[0]
            work_stages_list.append(work_stage_info["name"])

        print(f'#{index} {base_work["name"]} - wg({work_group_info["name"]}) - tg({tech_groups_list}) - ws({work_stages_list})')



wb.save(DIST_FILENAME)
