import string

import factory.fuzzy

from .models import *


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'name ' + str(n))
    password = factory.Sequence(lambda n: 'password' + str(n))
    email = factory.Sequence(lambda n: 'email' + str(n) + "@email.com")
    first_name = factory.Sequence(lambda n: 'first_name' + str(n))
    last_name = factory.Sequence(lambda n: 'last_name' + str(n))


class VehicleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Vehicle

    brand = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_uppercase + string.ascii_lowercase)
    model = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits)
    price = factory.fuzzy.FuzzyInteger(100, 1000)
    owner = factory.SubFactory(UserFactory, id=factory.fuzzy.FuzzyInteger(1, 10000))
    production_year = factory.fuzzy.FuzzyInteger(1850, timezone.now().year + 2)
    city = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_uppercase + string.ascii_lowercase)
    street = factory.fuzzy.FuzzyText(length=10, chars=string.ascii_uppercase + string.ascii_lowercase)
    power = factory.fuzzy.FuzzyInteger(40, 500)
    capacity = factory.fuzzy.FuzzyInteger(1, 8)
    drive_train = factory.fuzzy.FuzzyChoice(['FWD', 'AWD', 'RWD'])
    description = factory.Sequence(lambda n: 'description ' + str(n))


class ReservationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Reservation

    owner = factory.SubFactory(UserFactory, id=factory.fuzzy.FuzzyInteger(1, 10000))
    client = factory.SubFactory(UserFactory, id=factory.fuzzy.FuzzyInteger(10000, 20000))
    car = factory.SubFactory(VehicleFactory, owner=owner)
    start_date = factory.fuzzy.FuzzyDate(timezone.now(), timezone.now() + timezone.timedelta(days=1))
    end_date = factory.fuzzy.FuzzyDate(timezone.now() + timezone.timedelta(days=2),
                                       timezone.now() + timezone.timedelta(days=10))
    active = False
    message = factory.fuzzy.FuzzyText(length=20, chars=string.ascii_uppercase + string.ascii_lowercase)
