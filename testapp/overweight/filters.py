import django_filters

from .models import *


class TripFilter(django_filters.FilterSet):
    class Meta:
        model = TruckTrip
        fields = ['model_name']

    def __init__(self, *args, **kwargs):
        super(TripFilter, self).__init__(*args, **kwargs)
        self.filters['model_name'].label = "Модель"
        self.filters['model_name'].extra.update(
            {'empty_label': None})

