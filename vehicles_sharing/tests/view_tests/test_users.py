import pytest
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from . import urls_factory
from ...factories import VehicleFactory, UserFactory
from ...helpers import PomMethods as pm
from django.utils import timezone as tz


@pytest.mark.django_db
def test_log_in_1(client):
    user_id = 1
    user = UserFactory(id=user_id)
    password = "password69"
    user.password = make_password(password)
    user.save()
    expected_token = pm.get_token_from_user_id(user.id)

    # when
    response = client.post(urls_factory.url_not_detail(urls_factory.USERS, method="login"),
                           data={'username': user.username, 'password': password})

    # then
    assert response.status_code == 200
    assert expected_token.key == response.data


@pytest.mark.django_db
def test_log_in_2(client):
    user_id = 1
    user = UserFactory(id=user_id)
    password = "password69"
    wrong_password = "wrong_password"
    user.password = make_password(password)
    user.save()
    expected_message = "Invalid username or password"

    # when
    response = client.post(urls_factory.url_not_detail(urls_factory.USERS, method="login"),
                           data={'username': user.username, 'password': wrong_password})

    # then
    assert response.status_code == 400
    assert expected_message == response.data[0]
