# Generated by Django 3.2.13 on 2022-06-17 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overweight', '0005_auto_20220617_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='model',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='overweight.truckmodel'),
        ),
    ]
