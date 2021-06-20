from rest_framework import serializers
from .models import Directory, ElementOfDirectory


# Сериалайзер для модели Directory Справочника
class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = '__all__'


# Сериалайзер для модели ElementOfDirectory Элемента Справочника
class ElementOfDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementOfDirectory
        fields = '__all__'
