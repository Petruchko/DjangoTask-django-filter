from django.db import models


class TruckModel(models.Model):
    model_name = models.CharField('Модель самосвала', max_length=200, default='', null=True)
    capacity = models.IntegerField('Максимальная грузоподъемность', default=0, null=True)

    def __str__(self):
        return self.model_name


class Truck(models.Model):
    truck_name = models.CharField('Название самосвала', max_length=200)
    model_name = models.ForeignKey(TruckModel, on_delete=models.CASCADE, default=0, null=True)

    def __str__(self):
        return self.truck_name


class TruckTrip(models.Model):
    truck_name = models.ForeignKey(Truck, on_delete=models.CASCADE, default='', null=True)
    model_name = models.ForeignKey(TruckModel, db_column='Модель', on_delete=models.CASCADE, default='', null=True)
    weight = models.IntegerField('Текущий вес', default=0)

    def calculate_overweight(self):
        if self.weight > self.model_name.capacity:
            return round((self.weight - self.model_name.capacity) / self.model_name.capacity * 100, 2)
        else:
            return 0

    def __str__(self):
        return self.truck.truck_name + ": " + self.model.model_name


