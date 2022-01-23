import datetime
import math

from src.db import DataBaseUtils


def create_estimate():
    estimate_model = DataBaseUtils.get_model('estimate')
    if estimate_model is None:
        return
    estimate_data = dict([('active', False), ('create_date', datetime.datetime.today())])
    estimate, meth = DataBaseUtils.get_or_insert(estimate_model, estimate_data)
    estimate_base_size_model = DataBaseUtils.get_model('estimate_base_size')
    data = {'estimate': estimate}
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


def calculate_estimate(id_estimate, data):
    estimate_model = DataBaseUtils.get_model('estimate')
    if estimate_model is None:
        return
    fio = data['client_info']
    use_base = data['use_base']
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                dict([('field', 'client_fio'), ('value', fio)]))
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                dict([('field', 'use_base'), ('value', use_base)]))
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                dict([('field', 'active'), ('value', True)]))
    project_id = None
    if 'project_id' in data.keys():
        project_id = data['project_id']
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    dict([('field', 'project'), ('value', project_id)]))
    # Проставляем номер равный id
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                dict([('field', 'number'), ('value', id_estimate)]))
    # Получаем технологии для расчёта кастомные или из проекта
    technologies_data = []
    if 'work_technologies' in data and not data['use_base']:
        estimate_technologies = data['work_technologies']
        technologies_data = [dict([('estimate', id_estimate), ('work_technology', work_technology_id)])
                             for work_technology_id in estimate_technologies]
    else:
        technologies_data = get_technology_estimate(id_estimate, project_id)
    # Собираем работы из технологий
    works = calc_estimate_works(technologies_data)
    work_model = DataBaseUtils.get_model('work')
    # Собираем дополнительные работы
    if 'additional_works' in data:
        additional_model = DataBaseUtils.get_model('estimate_additional')
        additional_works = data['additional_works']
        additional_data = [dict([('estimate', id_estimate), ('work', work_id)]) for work_id in additional_works]
        for additional in additional_data:
            additional_work_id, _ = DataBaseUtils.get_or_insert(additional_model, additional)
            additional_work_object = DataBaseUtils.get_record(work_model, ({'id': additional['work']}))
            works.add(additional_work_object)
    # Обрабатываем работы
    estimate_price_client = calc_estimate_works_price(id_estimate, works, project_id)
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                dict([('field', 'price_client'), ('value', estimate_price_client)]))
    # Обрабатываем материалы
    estimate_price_client += calc_estimate_materials_price(id_estimate, project_id, works)
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                dict([('field', 'price_client'), ('value', estimate_price_client)]))


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


def delete_estimate(id_estimate):
    delete_additional_estimate(id_estimate)

    delete_estimate_technology(id_estimate)

    delete_estimate_work(id_estimate)

    delete_estimate_material(id_estimate)

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
            technologies_data = get_technology_estimate(id_estimate, project_id)
        else:
            # берём работы кастомные
            if 'work_technologies' in data and not use_base:
                estimate_technologies = data['work_technologies']
                technologies_data = [dict([('estimate', id_estimate), ('work_technology', work_technology_id)])
                                     for work_technology_id in estimate_technologies]
        # Собираем работы из технологий
        delete_estimate_technology(id_estimate)
        works = calc_estimate_works(technologies_data)
        work_model = DataBaseUtils.get_model('work')
        # Перезаписываем дополнительные работы
        if 'additional_works' in data:
            additional_model = DataBaseUtils.get_model('estimate_additional')
            additional_works = data['additional_works']
            additional_data = [dict([('estimate', id_estimate), ('work', work_id)])
                               for work_id in additional_works]
            delete_additional_estimate(id_estimate)
            for additional in additional_data:
                additional_work_id, _ = DataBaseUtils.get_or_insert(additional_model, additional)
                additional_work_object = DataBaseUtils.get_record(work_model, ({'id': additional['work']}))
                works.add(additional_work_object)
        delete_estimate_work(id_estimate)
        estimate_price_client = calc_estimate_works_price(id_estimate, works, project_id)
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    dict([('field', 'price_client'), ('value', estimate_price_client)]))
        delete_estimate_material(id_estimate)
        estimate_price_client += calc_estimate_materials_price(id_estimate, project_id, works)
        DataBaseUtils.update_record(estimate_model, id_estimate,
                                    dict([('field', 'price_client'), ('value', estimate_price_client)]))


def export_estimate(id_estimate):
    pass


def get_technology_estimate(estimate_id, project_id):
    project_technology_model = DataBaseUtils.get_model('project_technology')
    technologies_project = DataBaseUtils.get_records(project_technology_model, ({'project': project_id}))
    work_technologies = []
    for technology_project in technologies_project:
        work_technologies.append(technology_project.work_technology)
    return [dict([('estimate', estimate_id), ('work_technology', work_technology.id)])
            for work_technology in work_technologies]


def calc_estimate_works(technologies_data) -> set:
    # Собираем работы из технологий выбранных для расчёта
    estimate_technologies_model = DataBaseUtils.get_model('estimate_technology')
    works = set()
    work_model = DataBaseUtils.get_model('work')
    for technology in technologies_data:
        technologies_obj, _ = DataBaseUtils.get_or_insert(estimate_technologies_model, technology)
        technology_group_model = DataBaseUtils.get_model('technology_group')
        tech_groups = DataBaseUtils.get_records(technology_group_model,
                                                ({'work_technology': technology['work_technology']}))
        for tech_group in tech_groups:
            tech_group_objects = DataBaseUtils.get_records(technology_group_model,
                                                           ({'work_group': tech_group.work_group.id}))
            for tech_group_object in tech_group_objects:
                works.update(DataBaseUtils.get_records(work_model, ({'work_group': tech_group_object.work_group.id})))
    return works


def calc_estimate_works_price(id_estimate, works, project_id) -> int:
    estimate_model = DataBaseUtils.get_model('estimate')
    estimate_price_client = 0
    estimate_price_base = 0
    estimate_work_model = DataBaseUtils.get_model('estimate_work')
    base_size_model = DataBaseUtils.get_model('base_size')
    for work_object in works:
        work_client_price = 0
        work_base_price = 0
        # формулы расчёта цены работ
        if not work_object.fix_price:
            base_size = DataBaseUtils.get_record(base_size_model,
                                                 ({'project': project_id, 'base_unit': work_object.base_unit}))
            work_client_price = (work_object.client_price * base_size.amount)
            work_base_price = (work_object.work_price * base_size.amount)
        else:
            work_client_price = work_object.client_price
            work_base_price = work_object.work_price
        # Добавляем работу в EstimateWork
        work_data = dict([('estimate', id_estimate), ('work', work_object.id),
                          ('client_price', work_client_price), ('base_price', work_base_price)])
        DataBaseUtils.get_or_insert(estimate_work_model, work_data)
        estimate_price_client += work_client_price
        estimate_price_base += work_base_price
    # Заполняем цены для расчёта
    DataBaseUtils.update_record(estimate_model, id_estimate,
                                dict([('field', 'price_base'), ('value', estimate_price_base)]))
    return estimate_price_client


def calc_estimate_materials_price(id_estimate, project_id, works) -> int:
    work_material_model = DataBaseUtils.get_model('work_material')
    product_model = DataBaseUtils.get_model('product')
    estimate_work_model = DataBaseUtils.get_model('estimate_material')
    base_size_model = DataBaseUtils.get_model('base_size')
    estimate_price_client = 0
    for work in works:
        work_material_data = DataBaseUtils.get_records(work_material_model,
                                                       ({'work': work.id}))
        for work_material in work_material_data:
            base_size = DataBaseUtils.get_record(base_size_model,
                                                 ({'project': project_id, 'base_unit': work_material.work.base_unit}))
            product_obj = DataBaseUtils.get_record(product_model, ({'material': work_material.material.id}))
            if product_obj:
                # формулы расчёта материалов
                amount_product = math.ceil(((work_material.amount * base_size.amount) / product_obj.amount_for_one))
                material_price = amount_product * product_obj.price * work_material.material_coefficient
                estimate_material_data = dict([('estimate', id_estimate), ('product', product_obj.id),
                                               ('price', material_price), ('amount', amount_product)])
                DataBaseUtils.get_or_insert(estimate_work_model, estimate_material_data)
                estimate_price_client += material_price
    return estimate_price_client


def delete_additional_estimate(id_estimate):
    estimate_additional_model = DataBaseUtils.get_model('estimate_additional')
    estimate_additional_records = DataBaseUtils.get_records(estimate_additional_model, ({'estimate': id_estimate}))
    for estimate_additional in estimate_additional_records:
        DataBaseUtils.delete_record(estimate_additional_model, estimate_additional)


def delete_estimate_technology(id_estimate):
    estimate_technology_model = DataBaseUtils.get_model('estimate_technology')
    estimate_technology_records = DataBaseUtils.get_records(estimate_technology_model, ({'estimate': id_estimate}))
    for estimate_technology in estimate_technology_records:
        DataBaseUtils.delete_record(estimate_technology_model, estimate_technology)


def delete_estimate_work(id_estimate):
    estimate_work_model = DataBaseUtils.get_model('estimate_work')
    estimate_work_records = DataBaseUtils.get_records(estimate_work_model, ({'estimate': id_estimate}))
    for estimate_work in estimate_work_records:
        DataBaseUtils.delete_record(estimate_work_model, estimate_work)


def delete_estimate_material(id_estimate):
    estimate_material_model = DataBaseUtils.get_model('estimate_material')
    estimate_material_records = DataBaseUtils.get_records(estimate_material_model, ({'estimate': id_estimate}))
    for estimate_material in estimate_material_records:
        DataBaseUtils.delete_record(estimate_material_model, estimate_material)


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
