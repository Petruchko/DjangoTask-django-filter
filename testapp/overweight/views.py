from .models import TruckTrip
from django.shortcuts import render
from .filters import TripFilter


def table(request):  # Рисуем таблицу
    trips = TruckTrip.objects.all()
    my_filter = TripFilter(request.GET, queryset=trips)
    trips = my_filter.qs
    context = {
               'myFilter': my_filter,
               'trips': trips
               }
    return render(request, 'overweight/index.html', context)





