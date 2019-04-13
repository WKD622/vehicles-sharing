import pytest
from django.test import TestCase

from vehicles_sharing.factories import VehicleFactory, UserFactory
from vehicles_sharing.serializers import VehicleSerializer


class TestBrand(TestCase):
    @pytest.mark.django_db
    def test_brand_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand="Opel1"))
        # import pdb; pdb.set_trace()
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand="1Opel"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand="Opel1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand="1Opel ???"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand=" . 1Opel ???"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_6(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand="Opel 1"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand="Opel"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_brand_7(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, brand="Mercedes-Benz"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()


class TestModel(TestCase):
    @pytest.mark.django_db
    def test_model_1(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, model="190"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_model_2(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, model="gtx400"))
        serializer = VehicleSerializer(data=vehicle)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_model_3(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, model="190>?"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_model_4(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, model="190 (??"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()

    @pytest.mark.django_db
    def test_model_5(self):
        user_id = 1
        user = UserFactory(id=user_id)
        vehicle = vars(VehicleFactory(owner_id=user, model=" . 190 ???"))
        serializer = VehicleSerializer(data=vehicle)
        assert not serializer.is_valid()
