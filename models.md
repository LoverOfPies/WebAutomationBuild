# API Model

## get data
```
method: get

/get/:collection?filter_field1=2&filter_field2=33
```
## add data
```
method: post

/:collection
```
### get
```json
{
  "field1": "String (field1 value)",
  "field2": "String (field2 value)",
  "field3": "String (value)",
  ...
}
```
### return
```
json
[{
  "id": "String (id)",
  "field1": "String (field2 value)",
  "field2": "String (field2 value)",
  "uuid": "String (uuid)",
  ...
}]
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
```
method: get

/get_dict/<string:collection>
```

```json

  {
    "title": "TableInfo - title",
    "fields": [
      { "key": "String (Table Column Key)", "label": "String", "sortable": false },
      { "key": "name", "label": "String", "sortable": true },
      { "key": "product", "label": "String", "type": "selectable"}
    ],
    "filters": [
      {
        "key": "String (route name)",
        "label": "String",
        "multiple": "String во множественном числе"
      },
      {
        "key": "city",
        "label": "Город",
        "multiple": "Города"
      },
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
  }

```

# /import
```
method: post

/import/<string:collection>
```

```
request.file
```