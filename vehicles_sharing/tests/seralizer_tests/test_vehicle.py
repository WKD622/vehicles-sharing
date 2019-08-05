import pytest
from django.test import TestCase
from django.utils import timezone as tz

from vehicles_sharing.factories import VehicleFactory, UserFactory
from vehicles_sharing.serializers import VehicleSerializer


class TestBrand(TestCase):
    @pytest.mark.django_db
    def test_brand_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="Opel1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="1Opel"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="Opel1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="1Opel ???"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand=" . 1Opel ???"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="Opel 1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="Opel"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="Mercedes-Benz"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_8(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, brand="12213123"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_9(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['brand'] = 1000
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()


class TestModel(TestCase):
    @pytest.mark.django_db
    def test_model_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, model="190"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_model_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, model="gtx400"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_model_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, model="190>?"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_model_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, model="190 (??"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_model_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, model=" . 190 ???"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_model_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, model="Focus"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()


class TestPrice(TestCase):
    @pytest.mark.django_db
    def test_price_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, price=3000001))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_price_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, price=-1))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_price_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, price=0))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_price_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, price=3000000))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_price_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, price=1000))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_price_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['price'] = "string"
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()


class TestProductionYear(TestCase):
    @pytest.mark.django_db
    def test_production_year_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, production_year=tz.now().year + 3))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_production_year_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, production_year=-1))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_production_year_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, production_year=tz.now().year + 2))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_production_year_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, production_year=1799))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_production_year_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, production_year=1800))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_production_year_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, production_year=2010))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_production_year_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['production_year'] = "string"
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_production_year_8(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['production_year'] = "123"
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()


class TestDriveTrain(TestCase):
    @pytest.mark.django_db
    def test_drive_train_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='FWD'))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='AWD'))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='RWD'))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='fwd'))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='awd'))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='rwd'))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='1213'))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_8(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='FWD ?'))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_9(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='FWD1'))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_drive_train_10(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, drive_train='FWD 1'))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()


class TestCapacity(TestCase):
    @pytest.mark.django_db
    def test_capacity_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, capacity=1))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_capacity_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, capacity=8))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_capacity_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, capacity=5))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_capacity_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, capacity=0))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_capacity_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, capacity=9))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_capacity_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, capacity=12000))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_capacity_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, capacity=-10))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_capacity_8(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['capacity'] = "string"
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()


class TestPower(TestCase):
    @pytest.mark.django_db
    def test_power_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, power=0))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_power_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, power=10000))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_power_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, power=500))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_power_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, power=-1))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_power_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, power=10001))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_power_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, power=122222))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_power_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['power'] = "string"
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()


class TestCity(TestCase):
    @pytest.mark.django_db
    def test_city_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="Krakow"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_city_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="London"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_city_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="London1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_city_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="London 1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_city_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="London."))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_city_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="London ?"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_city_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="cos-cos"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_city_8(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['city'] = 213123
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()


class TestStreet(TestCase):
    @pytest.mark.django_db
    def test_street_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="Dietla"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_street_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="Nanannanaanananana"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_street_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="Dietla1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_street_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city="Dietla 1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_street_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city=".? Dietla"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_street_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user, city=".&&Dietla1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_street_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner=user))
        vehicle['street'] = 123123
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()