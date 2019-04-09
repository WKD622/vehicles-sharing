import factory.fuzzy
from .models import *


class VehicleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Vehicle

    brand = factory.Sequence(lambda n: 'brand ' + str(n))
    model = factory.Sequence(lambda n: 'model ' + str(n))
    price = factory.fuzzy.FuzzyInteger(100, 1000)
    owner_id = factory.Sequence(lambda n: str(n))
    production_year = factory.fuzzy.FuzzyInteger(100, 1000)
    city = factory.Sequence(lambda n: 'city ' + str(n))
    street = factory.Sequence(lambda n: 'street ' + str(n))
    power = factory.fuzzy.FuzzyInteger(40, 500)
    capacity = factory.fuzzy.FuzzyInteger(1, 8)
    drive_train = "TODO"
    description = factory.Sequence(lambda n: 'description ' + str(n))
