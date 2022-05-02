# WebAutomationBuild

# BackEnd

### Локальный запуск
```shell
> cd venv/scripts
> activate
> cd ../..
> python3 main.py
```

## TODO: 
- [ ] Перенести из models документацию
>Оформить нормальную документацию по работе с апи

- [ ] Удалить table_info.json


# FrontEnd

Запустить live-сервер: ```npm run start```

Собрать проект: ```npm run build```
>Проект собирается сразу в папку static

# Установка

Перед установкой собрать в папку `./app` папки: `migrations`, `src`, `static` а так же файлы: `app.py`, `config.json`, `main.py`, `requirements.txt`, `table_info.json`. Автосброщик завезем потом :)

### Собрать и запустить: 
```
docker-compose up --build
```
>Используй ```--no-start``` если необходимо восстановить дамп БД

### Пересобрать сервис представления
```
sudo docker-compose build --force-rm --no-cache
```
>Контейнер с БД будет не тронут

### Сохранение дампа БД
```
docker exec -i %pg_container_name% /bin/bash -c "PGPASSWORD=%pg_password% pg_dump --username %pg_username% %database_name%" > /your/path/to/dump.sql
```

### Восстановление дампа
```
docker exec -i %pg_container_name% /bin/bash -c "PGPASSWORD=%pg_password% psql --username %pg_username% %database_name%" < /your/path/to/dump.sql
```

Если при выполнении любой из команд возникает ошибка "нет доступа", ипользуй `sudo`