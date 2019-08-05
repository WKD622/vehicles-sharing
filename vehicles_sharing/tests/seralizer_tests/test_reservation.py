import pytest
from django.test import TestCase
from django.utils import timezone as tz
from django.core import serializers
from vehicles_sharing.factories import VehicleFactory, UserFactory, ReservationFactory
from vehicles_sharing.serializers import VehicleSerializer, ReservationSerializer
import json
from django.forms.models import model_to_dict

#
# class TestMessage(TestCase):
#     @pytest.mark.django_db
#     def test_message_1(self):
#         # import pdb; pdb.set_trace()
#         client_id = 1
#         owner_id = 2
#         client = UserFactory(id=client_id)
#         owner = UserFactory(id=owner_id)
#         vehicle = VehicleFactory(owner=owner)
#         reservation = model_to_dict(ReservationFactory(owner=owner, client=client, car=vehicle))
#         reservation['client'] = model_to_dict(client)
#         reservation['owner'] = model_to_dict(owner)
#         reservation['car'] = model_to_dict(vehicle)
#         import pdb;
#         pdb.set_trace()
#         serializer = ReservationSerializer(data=reservation)
#         assert serializer.is_valid()
