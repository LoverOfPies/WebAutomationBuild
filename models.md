# API Model

## get data
```
method: get

/:collection
```
## add data
```
method: post

/:collection
```
```json
{
  "field1": "String (field1 value)",
  "field2": "String (field2 value)",
  "foreign_uuid1": "String (value)",
  "foreign_uuid2": "String (value)",
  ...
}
```
## set data
```
method: put

/:collection/:id
```
```json
{
  "field": "String (field name)",
  "value": "String (value)"
}
```
## del data
```
method: delete

/:collection/:id
```

## sidebar
```
method: get

/sidebar

```


# sidebar.json
Пример выдачи элементов меню

```json
[
  {
    "title": "String",
    "icon": "String",
    "name": "String (route name)"
  },
  ...
]
```

# /info/route-name.json
Пример выдачи информации о разделе справочника по его `name`.

`mode` определяет вид таблицы

`simple` -- обычная таблица

`extended` -- таблица с настраиваемыми полями и фильтрами

Возможно есть смысл разделить фильтры? Я их еще не имплементировал. Но скорее всего обработка будет на серве, мозги уже есть. Так что нужно придумать как правильно посылать запросы на бэк :)

```json
[
    {
        "title": "String",
        "mode": "simple"
    },
    ...
]
```

```json
[
  {
    "title": "String",
    "mode": "extended",
    "fields": [
      { "key": "String (Table Row Key)", "label": "String", "sortable": false },
      { "key": "city", "label": "String", "sortable": true },
      { "key": "products", "label": "String" },
      { "key": "actions", "label": "String" }
    ],
    "filters": [
      {
        "key": "String (route name)",
        "label": "String",
        "multiple": "String во множественном числе"
      }
    ],
    "actions": [
      {
        "label": "String",
        "action": "String (route|delete)",
        "to": "String (route name if action == route)"
      },
      {
        "label": "Удалить (не обязательно для delete, стоит фоллбэк на всякий)",
        "action": "delete"
      }
    ]
  },
  ...
]
```

# /data/base-units.json
Пример выдачи списка базовых единиц

```json
[
    {
        "id": "Int",
        "name": "String"
    },
    ...
]
```

# /data/city.json example
Пример выдачи списка городов

```json
[
    {
        "id": "Int",
        "name": "String"
    },
    ...
]
```

# /data/providers.json
Пример выдачи списка поставщиков 

```json
[
    {
        "id": "Int",
        "name": "String",
        "city": "String",
        ...
    }
]
```

# /providers/:id/products
```json
[
  {
    "price": "Int",
    "amount": "Int",
    "material": "String"
  },
  {
    "price": "Int",
    "amount": "Int",
    "material": "String"
  },
  ...
]