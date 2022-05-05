import json

from migrations import (add_sidebar_column, edit_models_paths, add_sidebar_values)

# Таблица с миграциями, признаки выполнения в json
MIGRATIONS_LIST = {
    'add_sidebar_column': add_sidebar_column.run_script,
    'edit_models_paths': edit_models_paths.run_script,
    'add_sidebar_values': add_sidebar_values.run_script
}


# Читаем признак запуска скрипта
with open('migrations/migration_list.json', 'r', encoding='utf-8') as migration_info:
    migration_enable = json.load(migration_info)

# Запуск скриптов
for script_name, script in MIGRATIONS_LIST.items():
    if migration_enable[script_name] is 0:
        res = script()
        if res:
            migration_enable[script_name] = 1

# Проставить признак выполненным скриптам
with open('migrations/migration_list.json', 'w', encoding='utf-8') as migration_info:
    json.dump(migration_enable, migration_info)
