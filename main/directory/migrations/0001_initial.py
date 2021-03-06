# Generated by Django 3.2.4 on 2021-06-19 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование справочника')),
                ('short_name', models.CharField(max_length=150, verbose_name='Короткое наименование справочника')),
                ('description', models.TextField(verbose_name='Описание справочника')),
                ('version', models.CharField(max_length=50, unique=True, verbose_name='Описание справочника')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания справочника')),
            ],
            options={
                'verbose_name': 'Справочник',
                'verbose_name_plural': 'Справочники',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ElementOfDirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='Код элемента')),
                ('value', models.CharField(max_length=255, verbose_name='Значение элемента')),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.directory', verbose_name='Справочник элемента')),
            ],
            options={
                'verbose_name': 'Элемент справочника',
                'verbose_name_plural': 'Элементы справочника',
                'ordering': ('dictionary',),
            },
        ),
    ]
