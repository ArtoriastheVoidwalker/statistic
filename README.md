# README

This README would normally document whatever steps are necessary to get your application up and running.

### Инструкция по разворачиванию backend на локальном компьютере:

1. Склонировать проект
2. Перейти в репозиторий backend
3. Запустить *`./docker_prepare.sh`*
4. Для запуска backend перейти в корень папки и запустить `./dev.sh`
5. Запросы представленны в файле `Statistic.postman_collection.json`
6. Для запуска тестов `/scripts/test.sh`

**Описание методов и примеры вызова:**

Описание для endpoint ./endpoints/statistic.py:

`@router.post("/",response_model=schemas.Statistic)` - Роутер для приёма данных от клиента(Клиент вводит только:view,click,cost.Остальные поля будут заполненны автоматически). Для создание статистики в базе используется метод `save` , принимающий на вход данные из роутера. Пример запроса представлен в файле `Statistic.postman_collection.json`.

`@router.get(get_by_date"/",response_model=schemas.Statistics)` - Роутер для получение статистики,изходя из временного промежутка,заданного клиентом. В роутере происходит валидация введённых клиентом данных,после чего происходит запрос в базу данных,для этого используется метод `get_by_date`. Метод принимает на вход дату начала и дату конца периода статистик. Метод возвращает отсортированный по дате список из статистик за указанный период. Пример запроса:

`http://127.0.0.1:8000/api/v1/statistics/?from_date=2022-05-14&to_date=2022-06-14` - верёт статистику за месяц(с 14.05.2022 по 14.06.2022).

`@router.delete("/")` - Роутер для сброса статистики. Метод `get_multiget_multi` получает все записи из базы данных, затем, при помощи метода `remove`, циклично удаляет все записи. Пример запроса представлен в файле `Statistic.postman_collection.json`.Пример запроса представлен в файле `Statistic.postman_collection.json`.