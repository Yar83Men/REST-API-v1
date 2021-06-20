from django.contrib import admin
from .models import Directory, ElementOfDirectory


class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'description', 'version', 'date')
    search_fields = ('name', 'version')
    list_editable = ('name', 'short_name', 'description', 'version')


class ElementOfDirectoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'value', 'dictionary')
    search_fields = ('code', 'dictionary')
    list_editable = ('code', 'value')


admin.site.register(Directory, DirectoryAdmin)
admin.site.register(ElementOfDirectory, ElementOfDirectoryAdmin)
