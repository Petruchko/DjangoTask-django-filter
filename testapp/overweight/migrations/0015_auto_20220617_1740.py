# Generated by Django 3.2.13 on 2022-06-17 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overweight', '0014_alter_trucktrip_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truck',
            old_name='model',
            new_name='model_name',
        ),
        migrations.RenameField(
            model_name='trucktrip',
            old_name='model',
            new_name='model_name',
        ),
        migrations.RenameField(
            model_name='trucktrip',
            old_name='truck',
            new_name='truck_name',
        ),
    ]
