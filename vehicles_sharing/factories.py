import factory.fuzzy
from .models import *
from django.utils import timezone


class VehicleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Vehicle

    brand = factory.Sequence(lambda n: 'brand ' + str(n))
    model = factory.Sequence(lambda n: 'model ' + str(n))
    price = factory.fuzzy.FuzzyInteger(100, 1000)
    owner_id = factory.Sequence(lambda n: str(n))
    production_year = factory.fuzzy.FuzzyInteger(1850, timezone.now().year + 2)
    city = factory.Sequence(lambda n: 'city ' + str(n))
    street = factory.Sequence(lambda n: 'street ' + str(n))
    power = factory.fuzzy.FuzzyInteger(40, 500)
    capacity = factory.fuzzy.FuzzyInteger(1, 8)
    drive_train = factory.fuzzy.FuzzyChoice(['FWD', 'AWD', 'RWD'])
    description = factory.Sequence(lambda n: 'description ' + str(n))


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'name ' + str(n))
    password = factory.Sequence(lambda n: 'password' + str(n))
    email = factory.Sequence(lambda n: 'email' + str(n) + "@email.com")
