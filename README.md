# Test_KOMTEK
### Test KOMTEK final version API
## URLS
## api/directory/                   GET запрос, выдает json список всех Справочников
## api/directory/elements/          POST запрос содержит json {"version":"Версия"}, json - список Элементов Спарвочника указанной версии
## api/directory/current/           POST запросом передается имя Справочника {"name":"Имя справочника"}, json - список Элементов Справочника последней версии (последний по дате)
## api/directory/validate/          POST запрос {"version":"Версия Справочника", "code":"Код Элемента справочника"}
                                    Возвращает json - список Элементов справочника (если они есть в Справочнике) по указанной версии Справочника
## api/directory/validate/current   POST запрос {"name":"Имя справочника", "code":"Код эелемента справочника"}
                                    Возвращается json объект со списком Элементов (если они есть в Справочнике) с последней датой Справочника
## Дамп базы данных postgresql      directory_db.dump
## Имя базы данных                  directory_db
## Пользователь                     directory_admin
## Пароль                           root12345
                           

