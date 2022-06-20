# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-09 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overweight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='capacity',
            field=models.IntegerField(default=0, verbose_name='Максимальная грузоподъемность'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='model_name',
            field=models.CharField(max_length=200, verbose_name='Модель самосвала'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='truck_name',
            field=models.CharField(max_length=200, verbose_name='Название самосвала'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Текущий вес'),
        ),
    ]