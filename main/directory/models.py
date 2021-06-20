from django.db import models
from django.utils import timezone

# Класс модели Справочника
class Directory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование справочника')
    short_name = models.CharField(max_length=150, verbose_name='Короткое наименование справочника')
    description = models.TextField(verbose_name='Описание справочника')
    version = models.CharField(max_length=50, blank=False, unique=True, verbose_name="Версия справочника")
    date = models.DateTimeField(verbose_name="Дата создания справочника",  default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"
        ordering = ('name',)

# Класс модели Элемента справочника
class ElementOfDirectory(models.Model):
    dictionary = models.ForeignKey(Directory, on_delete=models.CASCADE, verbose_name="Справочник элемента")
    code = models.CharField(max_length=100, blank=False, verbose_name="Код элемента")
    value = models.CharField(max_length=255, blank=False, verbose_name="Значение элемента")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Элемент справочника"
        verbose_name_plural = "Элементы справочника"
        ordering = ('dictionary',)
