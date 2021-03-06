# Generated by Django 3.2.13 on 2022-06-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overweight', '0002_auto_20220609_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0, verbose_name='Текущий вес')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='overweight.truck')),
            ],
        ),
    ]
