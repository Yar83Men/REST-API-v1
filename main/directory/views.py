from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Directory, ElementOfDirectory
from .serializers import DirectorySerializer, ElementOfDirectorySerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

paginator = PageNumberPagination()
paginator.page_size = 10


# Получение списка справочников
# Метод GET url api/directory/
# Возвращает json объект - список всех Справочников
@api_view(['GET', 'POST'])
def directory_list(request):
    # Если запрос по GET по url api/directory/ , весь список в json
    if request.method == 'GET':
        directories = Directory.objects.all()
        result_page = paginator.paginate_queryset(directories, request)
        serializer = DirectorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    # Получение списка справочников, актуальных на указанную дату
    # Если запрос POST передается json {"date":"Y-m-d"} по url api/directory/
    # Возращается json - список Справочников по заданной дате
    elif request.method == 'POST':
        list_of_directories = Directory.objects.filter(date__contains=request.data['date'])

        if len(list_of_directories) == 0:
            return HttpResponse(status=404)

        result_page = paginator.paginate_queryset(list_of_directories, request)
        serializer = DirectorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


# Получение элементов заданного справочника указанной версии
# Функция представления списка Элементов Справочника при передаче POST запросом версии Справочника
# POST запрос содержит json {"version":"Версия"} , url api/directory/elements/
# Возвращает json - список Элементов Спарвочника указанной версии
@api_view(['GET','POST'])
def elements_of_directory(request):
    if request.method == 'GET':
        return Response(data='Метод POST {\'version\':\'Версия Справочника\'}')
    try:
        directory_id = Directory.objects.get(version=request.data['version']).id
    except Directory.DoesNotExist:
        return HttpResponse(status=404)

    list_of_elements = ElementOfDirectory.objects.filter(dictionary=directory_id)
    result_page = paginator.paginate_queryset(list_of_elements, request)
    serializer = ElementOfDirectorySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Получение элементов заданного справочника текущей версии
# Функция представления списка Элементов текущего Справочника
# POST запросом передается имя Справочника {"name":"Имя справочника"}, url api/directory/current/
# Возвращает json - список Элементов Справочника последней версии (последний по дате)
@api_view(['GET','POST'])
def elements_current_directory(request):
    if request.method == 'GET':
        return Response(data='Метод POST {\'name\':\'Название Справочника\'}')
    try:
        directory_name = Directory.objects.filter(name=request.data['name']).latest('date')
    except Directory.DoesNotExist:
        return HttpResponse(status=404)

    list_of_current_dictionary_elements = ElementOfDirectory.objects.filter(dictionary=directory_name.id)

    result_page = paginator.paginate_queryset(list_of_current_dictionary_elements, request)
    serializer = ElementOfDirectorySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Валидация элемента заданного справочника по указанной версии
# POST запрос api/directory/validate/ с передачей кода Элемента и версии Справочника
# JSON {"version":"Версия Справочника", "code":"Код Элемента справочника"}
# Возвращает json - список Элементов справочника (если они есть в Справочнике) по указанной версии Справочника
@api_view(['GET','POST'])
def validate_element(request):
    if request.method == 'GET':
        return Response(data='Метод POST {\'version\':\'Версия Справочника\', \'code\':\'Код Элемента справочника\'}')

    try:
        directory_id_by_version = Directory.objects.get(version=request.data['version']).id

    except Directory.DoesNotExist:
        return HttpResponse(status=404)

    try:
        validate_element = ElementOfDirectory.objects.filter(
            Q(code=request.data['code']) & Q(dictionary=directory_id_by_version))

    except ElementOfDirectory.DoesNotExist:
        return HttpResponse(status=404)

    result_page = paginator.paginate_queryset(validate_element, request)
    serializer = ElementOfDirectorySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Валидация элементов заданного справочника текущей версии
# POST запросом на url api/directory/validate/current посылается json
# {"name":"Имя справочника", "code":"Код эелемента справочника"}
# Возвращается json объект со списком Элементов (если они есть в Справочнике) с последней датой Справочника
@api_view(['GET', 'POST'])
def validate_current_element(request):
    if request.method == 'GET':
        return Response(data='Метод POST {\'name\':\'Имя Cправочника\', \'code\':\'Код Элемента справочника\'}')
    try:
        directory_name_latest = Directory.objects.filter(name=request.data['name']).latest('date')

    except Directory.DoesNotExist:
        return HttpResponse(status=404)

    try:
        validate_current_element = ElementOfDirectory.objects.filter(
            Q(code=request.data['code']) & Q(dictionary=directory_name_latest.id))

    except ElementOfDirectory.DoesNotExist:
        return HttpResponse(status=404)

    result_page = paginator.paginate_queryset(validate_current_element, request)
    serializer = ElementOfDirectorySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
