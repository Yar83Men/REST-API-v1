from django.urls import path
from .views import *

urlpatterns = [
    # GET запрос, выдает json список всех Справочников
    path('api/directory/', directory_list),
    # POST запрос содержит json {"version":"Версия"}, json - список Элементов Спарвочника указанной версии
    path('api/directory/elements/', elements_of_directory),
    # POST запросом передается имя Справочника {"name":"Имя справочника"},
    # json - список Элементов Справочника последней версии (последний по дате)
    path('api/directory/current/', elements_current_directory),
    # POST запрос {"version":"Версия Справочника", "code":"Код Элемента справочника"}
    # Возвращает json - список Элементов справочника (если они есть в Справочнике) по указанной версии Справочника
    path('api/directory/validate/', validate_element),
    # POST запрос {"name":"Имя справочника", "code":"Код эелемента справочника"}
    # Возвращается json объект со списком Элементов (если они есть в Справочнике) с последней датой Справочника
    path('api/directory/validate/current', validate_current_element),
]
