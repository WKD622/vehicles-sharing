import pytest
from rest_framework.utils import json
from . import urls_factory
from ...factories import VehicleFactory, UserFactory
from ...helpers import PomMethods as pm
from django.utils import timezone as tz


@pytest.mark.django_db
def test_log_in(client):
    # given
    user_id = 1
    user = UserFactory(id=user_id)
    expected_token = pm.get_token_from_user_id(user.id)

    # when
    response = client.post(urls_factory.url_not_detail(urls_factory.USERS, method="login"),
                           data={'username': user.username, 'password': user.password})

    # then
    assert response.status_code == 200
    assert expected_token == response.content
