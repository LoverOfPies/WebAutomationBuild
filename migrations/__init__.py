import json

from migrations import init_copy_work_group, actions_info_to_not_null

# Таблица с миграциями, признаки выполнения в json
MIGRATIONS_LIST = {
    'actions_info_to_not_null': actions_info_to_not_null.run_script,
    'init_copy_work_group': init_copy_work_group.run_script
}


# Читаем признак запуска скрипта
with open('migrations/migration_list.json', 'r', encoding='utf-8') as migration_info:
    migration_enable = json.load(migration_info)

# Запуск скриптов
for script_name, script in MIGRATIONS_LIST.items():
    if not migration_enable[script_name]:
        res = script()
        if res:
            migration_enable[script_name] = 1

# Проставить признак выполненным скриптам
with open('migrations/migration_list.json', 'w', encoding='utf-8') as migration_info:
    json.dump(migration_enable, migration_info)
