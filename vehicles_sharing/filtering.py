import django_filters
from django_filters import RangeFilter, ChoiceFilter, CharFilter
from .models import DRIVE_TRAIN_CHOICES

from vehicles_sharing.models import Vehicle


class VehicleFilter(django_filters.FilterSet):
    price = RangeFilter()
    power = RangeFilter()
    production_year = RangeFilter()
    capacity = RangeFilter()
    drive_train = ChoiceFilter(choices=DRIVE_TRAIN_CHOICES)
    city = CharFilter()
    brand = CharFilter()
    model = CharFilter()

    class Meta:
        model = Vehicle
        fields = ['price', 'power', 'production_year', 'capacity',
                  'drive_train', 'city', 'brand', 'model']
