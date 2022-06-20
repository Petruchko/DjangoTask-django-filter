from django.contrib import admin

from .models import Truck, TruckTrip, TruckModel

admin.site.register(Truck)
admin.site.register(TruckTrip)
admin.site.register(TruckModel)

# Register your models here.
