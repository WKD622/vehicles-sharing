import pytest
from rest_framework.utils import json
from . import urls_factory
from ...factories import VehicleFactory, UserFactory
from ...pom import PomMethods as pm
from django.utils import timezone as tz


@pytest.mark.django_db
def test_min_price(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(price=100, owner=user)
    expected_vehicle_1 = VehicleFactory(price=200, owner=user)
    expected_vehicle_2 = VehicleFactory(price=300, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'min_price': 150},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_max_price(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(price=300, owner=user)
    expected_vehicle_1 = VehicleFactory(price=100, owner=user)
    expected_vehicle_2 = VehicleFactory(price=200, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'max_price': 200},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_min_power(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(power=100, owner=user)
    expected_vehicle_1 = VehicleFactory(power=200, owner=user)
    expected_vehicle_2 = VehicleFactory(power=300, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'min_power': 101},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_max_power(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(power=300, owner=user)
    expected_vehicle_1 = VehicleFactory(power=100, owner=user)
    expected_vehicle_2 = VehicleFactory(power=200, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'max_power': 200},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_min_production_year(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    current_year = tz.now().year
    VehicleFactory(production_year=current_year - 10, owner=user)
    expected_vehicle_1 = VehicleFactory(production_year=current_year - 5, owner=user)
    expected_vehicle_2 = VehicleFactory(production_year=current_year - 1, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES),
                          data={'min_production_year': current_year - 6},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_max_production_year(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    current_year = tz.now().year
    VehicleFactory(production_year=current_year, owner=user)
    expected_vehicle_1 = VehicleFactory(production_year=current_year - 5, owner=user)
    expected_vehicle_2 = VehicleFactory(production_year=current_year - 2, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES),
                          data={'max_production_year': current_year - 2},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_min_capacity(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(capacity=2, owner=user)
    expected_vehicle_1 = VehicleFactory(capacity=4, owner=user)
    expected_vehicle_2 = VehicleFactory(capacity=5, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'min_capacity': 4},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_max_capacity(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(capacity=7, owner=user)
    expected_vehicle_1 = VehicleFactory(capacity=4, owner=user)
    expected_vehicle_2 = VehicleFactory(capacity=5, owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'max_capacity': 5},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_max_brand(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(brand='Opel', owner=user)
    expected_vehicle_1 = VehicleFactory(brand='Ford', owner=user)
    expected_vehicle_2 = VehicleFactory(brand='Ford', owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'brand': 'Ford'},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_max_brand(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(model='Passat', owner=user)
    VehicleFactory(model='Focus2', owner=user)
    expected_vehicle_1 = VehicleFactory(model='Focus', owner=user)
    expected_vehicle_2 = VehicleFactory(model='Focus', owner=user)
    expected_number_of_vehicles = 2
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'model': 'Focus'},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id, expected_vehicle_2.id}


@pytest.mark.django_db
def test_city(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(city='Kraków', owner=user)
    VehicleFactory(city='Warszawa', owner=user)
    expected_vehicle_1 = VehicleFactory(city='Opole', owner=user)
    expected_number_of_vehicles = 1
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'city': 'Opole'},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id}


@pytest.mark.django_db
def test_drive_train(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(drive_train='FWD', owner=user)
    VehicleFactory(drive_train='AWD', owner=user)
    expected_vehicle_1 = VehicleFactory(drive_train='RWD', owner=user)
    expected_number_of_vehicles = 1
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES), data={'drive_train': 'RWD'},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id}


@pytest.mark.django_db
def test_searching_model(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(brand='Mercedes', model="190", owner=user)
    VehicleFactory(brand='Opel', model="Vectra", owner=user)
    expected_vehicle_1 = VehicleFactory(brand='Opel', model="Astra", owner=user)
    expected_number_of_vehicles = 1
    token = pm.get_token_from_user_id(user_id)
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES, 'search'), data={'on': 'Astra'},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id}


@pytest.mark.django_db
def test_searching_model_brand(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(brand='Mercedes', model="Astra", owner=user)
    VehicleFactory(brand='Opel', model="Vectra", owner=user)
    expected_vehicle_1 = VehicleFactory(brand='Opel', model="Astra", owner=user)
    expected_number_of_vehicles = 1
    token = pm.get_token_from_user_id(user_id)
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES, 'search'), data={'on': 'Opel Astra'},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id}


@pytest.mark.django_db
def test_searching_brand(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    VehicleFactory(brand='Mercedes', model="190", owner=user)
    VehicleFactory(brand='Mercedes', model="W123", owner=user)
    expected_vehicle_1 = VehicleFactory(brand='Opel', model="Astra", owner=user)
    expected_number_of_vehicles = 1
    token = pm.get_token_from_user_id(user_id)
    headers = {
        f'Authorization': 'Token {pm.get_token_from_user_id(user_id)}'
    }

    # when
    response = client.get(urls_factory.url_not_detail(urls_factory.VEHICLES, 'search'), data={'on': 'Opel'},
                          headers=headers)
    vehicles = list()

    for x in json.loads(response.content):
        vehicles.append(x['id'])

    # then
    assert response.status_code == 200
    assert expected_number_of_vehicles == len(vehicles)
    assert set(vehicles) == {expected_vehicle_1.id}
