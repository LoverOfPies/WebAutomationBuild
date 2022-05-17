import datetime
import math
from typing import List

from peewee import Model

from api.base import DataBaseUtils
from api.base.MyAppException import MyAppException


def create_estimate() -> int:
    """
    Метод для инициализации расчёта по кнопке "Добавить" на интерфейсе расчёта

    :return: estimate_id (int) - ид созданного расчёта
    """
    # Создаём новый расчёт
    estimate_model: Model = DataBaseUtils.get_model('estimate')
    estimate_data: dict = {'active': False, 'create_date': datetime.datetime.today()}
    estimate = DataBaseUtils.insert_record(estimate_model, estimate_data)

    # Проставляем все возможные базовые единицы, как базовые размеры расчёта с значением 0
    estimate_base_size_model = DataBaseUtils.get_model('estimate_base_size')
    data = {'estimate': estimate.id}
    base_units = DataBaseUtils.get_records(DataBaseUtils.get_model('base_unit'), '')
    for base_unit in base_units:
        data['base_unit'] = base_unit
        DataBaseUtils.get_or_insert(estimate_base_size_model, data)

    return estimate


def get_estimate_records():
    model = DataBaseUtils.get_model('estimate')
    if model is None:
        return None
    return [row for row in model.select().dicts()]


def calculate_estimate(id_estimate: int, data: dict):
    # Получаем модель расчёта в БД
    # TODO: Сделать обработку в одной транзакции
    estimate_model = DataBaseUtils.get_model('estimate')
    if estimate_model is None:
        return

    fio = data['client_info']
    if not fio:
        raise MyAppException('Не заполнено поле ФИО')
    use_base = data['use_base']
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                {'field': 'client_fio', 'value': fio})
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                {'field': 'use_base', 'value': use_base})
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                {'field': 'active', 'value': True})

    # Смотрим наличие проекта и привязываем, если есть
    project_id = data.get('project_id', None)
    if project_id:
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    {'field': 'project', 'value': project_id})

    # Проставляем номер равный id
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                {'field': 'number', 'value': id_estimate})

    # Получаем технологии для расчёта кастомные или из проекта
    technologies_data = []
    if 'work_technologies' in data and not data['use_base']:
        technologies_data = [{'estimate': id_estimate, 'work_technology': work_technology_id}
                             for work_technology_id in data['work_technologies']]
    else:
        technologies_data = get_technology_from_project(id_estimate, project_id)

    # Собираем работы из технологий
    works = calc_estimate_works(technologies_data)
    work_model = DataBaseUtils.get_model('work')
    # Собираем дополнительные работы
    if 'additional_works' in data:
        additional_model = DataBaseUtils.get_model('estimate_additional')
        additional_works = data['additional_works']
        for work_id in additional_works:
            DataBaseUtils.get_or_insert(additional_model, {'estimate': id_estimate, 'work': work_id})
            additional_work_object = DataBaseUtils.get_record(work_model, {'id': work_id})
            works.append(additional_work_object)
    # Обрабатываем работы
    estimate_price_client = __calc_estimate_works_price(id_estimate, works, project_id)
    # Обрабатываем материалы
    estimate_price_client += __calc_estimate_materials_price(id_estimate, project_id, works)
    # Записываем цену клиента в БД
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                {'field': 'price_client', 'value': estimate_price_client})


def get_estimate_materials(id_estimate):
    model = DataBaseUtils.get_model('estimate_material')
    if model is None:
        return None
    data = [row for row in model.select().where(model.estimate == id_estimate).dicts()]
    product_model = DataBaseUtils.get_model('product')
    for value in data:
        product = DataBaseUtils.get_record(product_model, {'id': value['product']})
        value['material_name'] = product.material.name
    return data


def get_estimate_works(id_estimate):
    model = DataBaseUtils.get_model('estimate_work')
    if model is None:
        return None
    data = [row for row in model.select().where(model.estimate == id_estimate).dicts()]
    work_model = DataBaseUtils.get_model('work')
    for value in data:
        work = DataBaseUtils.get_record(work_model, {'id': value['work']})
        value['work_name'] = work.name
    return data


def delete_estimate(id_estimate: int):
    """
    Метод для удаления расчёта по кнопке "Удалить" на интерфейсе расчёта

    :param: id_estimate (int) ид расчёта
    """
    # Удаляем дополнительные работы для расчёта
    cascade_delete_estimate(id_estimate, 'estimate_additional')
    # Удаляем основные технологии работ для расчёта
    cascade_delete_estimate(id_estimate, 'estimate_technology')
    # Удаляем основные работы работ для расчёта
    cascade_delete_estimate(id_estimate, 'estimate_work')
    # Удаляем материалы для расчёта
    cascade_delete_estimate(id_estimate, 'estimate_material')
    # Удаляем расчёт
    estimate_model = DataBaseUtils.get_model('estimate')
    estimate_record = DataBaseUtils.get_record(estimate_model, ({'id': id_estimate}))
    DataBaseUtils.delete_record(estimate_model, estimate_record)


def edit_estimate(id_estimate, data):
    estimate_model = DataBaseUtils.get_model('estimate')
    estimate_object = DataBaseUtils.get_record(estimate_model, ({'id': id_estimate}))
    if estimate_model is None:
        return
    fio = data['client_info']
    if fio != estimate_object.client_fio:
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    dict([('field', 'client_fio'), ('value', fio)]))
    use_base = data['use_base']
    project_id = None
    if 'project_id' in data.keys():
        project_id = data['project_id']
        if project_id != estimate_object.project.id:
            DataBaseUtils.update_record(estimate_model, id_estimate,
                                        dict([('field', 'project'), ('value', project_id)]))
    if use_base != estimate_object.use_base or project_id != estimate_object.project.id:
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    dict([('field', 'use_base'), ('value', use_base)]))
        technologies_data = []
        if use_base:
            # берём работы у проекта
            technologies_data = get_technology_from_project(id_estimate, project_id)
        else:
            # берём работы кастомные
            if 'work_technologies' in data and not use_base:
                estimate_technologies = data['work_technologies']
                technologies_data = [dict([('estimate', id_estimate), ('work_technology', work_technology_id)])
                                     for work_technology_id in estimate_technologies]
        # Собираем работы из технологий
        cascade_delete_estimate(id_estimate, 'estimate_technology')
        works = calc_estimate_works(technologies_data)
        work_model = DataBaseUtils.get_model('work')
        # Перезаписываем дополнительные работы
        if 'additional_works' in data:
            additional_model = DataBaseUtils.get_model('estimate_additional')
            additional_works = data['additional_works']
            additional_data = [dict([('estimate', id_estimate), ('work', work_id)])
                               for work_id in additional_works]
            cascade_delete_estimate(id_estimate, 'estimate_additional')
            for additional in additional_data:
                additional_work_id, _ = DataBaseUtils.get_or_insert(additional_model, additional)
                additional_work_object = DataBaseUtils.get_record(work_model, ({'id': additional['work']}))
                works.add(additional_work_object)
        cascade_delete_estimate(id_estimate, 'estimate_work')
        estimate_price_client = __calc_estimate_works_price(id_estimate, works, project_id)
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    dict([('field', 'price_client'), ('value', estimate_price_client)]))
        cascade_delete_estimate(id_estimate, 'estimate_material')
        estimate_price_client += __calc_estimate_materials_price(id_estimate, project_id, works)
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    dict([('field', 'price_client'), ('value', estimate_price_client)]))


def export_estimate(id_estimate):
    pass


def get_technology_from_project(estimate_id: int, project_id: int) -> List[dict]:
    project_technology_model = DataBaseUtils.get_model('project_technology')
    technologies_project = DataBaseUtils.get_records(project_technology_model, {'project': project_id})
    return [{'estimate': estimate_id, 'work_technology': technology_project.work_technology.id}
            for technology_project in technologies_project]


def calc_estimate_works(technologies_data) -> list:
    # Собираем работы из технологий выбранных для расчёта
    estimate_technologies_model = DataBaseUtils.get_model('estimate_technology')

    # Получаем ид групп работ
    work_group_ids = []
    for technology in technologies_data:
        DataBaseUtils.get_or_insert(estimate_technologies_model, technology)
        technology_group_model = DataBaseUtils.get_model('technology_group')
        tech_groups = DataBaseUtils.get_records(technology_group_model,
                                                {'work_technology': technology['work_technology']})
        work_group_ids += [tech_group.work_group.id for tech_group in tech_groups]

    # Получаем список работ
    works = []
    work_model = DataBaseUtils.get_model('work')
    for work_group_id in work_group_ids:
        works.extend(DataBaseUtils.get_records(work_model, {'work_group': work_group_id}))
    return works


def __calc_estimate_works_price(id_estimate, works, project_id) -> int:
    """

    """
    # Инициализация моделей
    estimate_model = DataBaseUtils.get_model('estimate')
    estimate_work_model = DataBaseUtils.get_model('estimate_work')
    base_size_model = DataBaseUtils.get_model('base_size')
    # Инициализация переменных цен для расчёта
    estimate_price_client = 0
    estimate_price_base = 0

    for work_object in works:
        # Инициализация переменных цен для отдельной работы
        work_client_price = work_object.client_price
        work_base_price = work_object.work_price

        # Если цена не фиксированная, то высчитываем по базовому размеру из проекта
        # TODO: Базовые единицы привязываем теперь к расчёту
        if not work_object.fix_price:
            base_size = DataBaseUtils.get_record(base_size_model,
                                                 {'project': project_id, 'base_unit': work_object.base_unit})
            work_client_price = (work_object.client_price * base_size.amount)
            work_base_price = (work_object.work_price * base_size.amount)

        # Добавляем работу в EstimateWork (связка расчёта и работ)
        work_data = {'estimate': id_estimate, 'work': work_object.id,
                     'client_price': work_client_price, 'base_price': work_base_price}
        DataBaseUtils.get_or_insert(estimate_work_model, work_data)
        # Прибавляем цену работы к общей цене
        estimate_price_client += work_client_price
        estimate_price_base += work_base_price
    # Записываем цены для расчёта в БД
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                {'field', 'price_base', 'value', estimate_price_base})
    return estimate_price_client


def __calc_estimate_materials_price(id_estimate, project_id, works) -> int:
    # Инициализация данных
    work_material_model = DataBaseUtils.get_model('work_material')
    product_model = DataBaseUtils.get_model('product')
    estimate_work_model = DataBaseUtils.get_model('estimate_material')
    base_size_model = DataBaseUtils.get_model('base_size')
    estimate_price_client = 0
    # Получаем все материалы для работ
    work_materials = []
    for work in works:
        work_materials.extend(DataBaseUtils.get_records(work_material_model, {'work': work.id}))

    # Считаем стоимость материалов
    for work_material in work_materials:
        base_size = DataBaseUtils.get_record(base_size_model,
                                             {'project': project_id, 'base_unit': work_material.work.base_unit})
        product_obj = DataBaseUtils.get_record(product_model, {'material': work_material.material.id})
        if product_obj:
            # Количестов единиц материала по размерам
            material_to_base_size = work_material.amount * base_size.amount
            # Количество упаковок
            amount_product_pack = math.ceil((material_to_base_size / product_obj.amount_for_one))
            # Стоимость материала с учётом коэффицента
            material_price = amount_product_pack * product_obj.price * work_material.material_coefficient
            # Записываем данные расчёта в БД
            estimate_material_data = {'estimate': id_estimate, 'product': product_obj.id,
                                      'price': material_price, 'amount': amount_product_pack}
            DataBaseUtils.get_or_insert(estimate_work_model, estimate_material_data)
            # Прибавляем к общей стоимости материалов
            estimate_price_client += material_price
    return estimate_price_client


def cascade_delete_estimate(id_estimate: int, collection: str) -> None:
    """
    Метод для каскадного удаления из таблиц связанных с расчётом

    :param: id_estimate (int) ид расчёта
    """
    cascade_model: Model = DataBaseUtils.get_model(collection)
    cascade_records: List[object] = \
        DataBaseUtils.get_records(cascade_model, {'estimate': id_estimate})
    for cascade_record in cascade_records:
        DataBaseUtils.delete_record(cascade_model, cascade_record)


def get_project_technologies(id_project):
    model = DataBaseUtils.get_model('project_technology')
    if model is None:
        return None
    data = [row for row in model.select().where(model.project == id_project).dicts()]
    work_technology_model = DataBaseUtils.get_model('work_technology')
    for value in data:
        work_technology = DataBaseUtils.get_record(work_technology_model, {'id': value['work_technology']})
        del value['id']
        del value['uuid']
        del value['project']
        value['work_technology_name'] = work_technology.name
        value['work_stage'] = work_technology.work_stage.id
        value['work_stage_name'] = work_technology.work_stage.name
    return data
