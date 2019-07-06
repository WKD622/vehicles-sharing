from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone
from rest_framework import serializers

from .models import Vehicle, Reservation, Photo
from .helpers import Validators as validators
from datetime import datetime


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.IntegerField(min_value=0, max_value=3000000)
    production_year = serializers.IntegerField(min_value=1800, max_value=timezone.now().year + 2)
    description = serializers.CharField(max_length=10000)
    brand = serializers.CharField(max_length=50, validators=[validators.brand])
    model = serializers.CharField(max_length=50, validators=[validators.alphanumeric])
    drive_train = serializers.CharField(min_length=3, max_length=3, validators=[validators.drive_train])
    capacity = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    power = serializers.IntegerField(allow_null=True, min_value=0, max_value=10000)
    city = serializers.CharField(max_length=50, validators=[validators.city_street])
    street = serializers.CharField(max_length=50, validators=[validators.city_street])

    class Meta:
        model = Vehicle
        fields = (
            'id', 'brand', 'model', 'price', 'production_year', 'description', 'drive_train', 'city', 'street', 'power',
            'capacity')


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    client = UserSerializer(many=False)
    car = VehicleSerializer(many=False)
    owner = UserSerializer(many=False)
    message = serializers.CharField(max_length=3000)
    active = serializers.BooleanField(required=True)
    start_date = serializers.DateField(format="iso-8601", input_formats=['iso-8601'])
    end_date = serializers.DateField(format="iso-8601", input_formats=['iso-8601'])
    reservation_on_my_vehicle = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            'start_date', 'end_date', 'active', 'message', 'id', 'client', 'owner', 'car', 'reservation_on_my_vehicle')
        extra_kwargs = {
            'client': {
                'validators': []
            },
            'owner': {
                'validators': []
            },
            'car': {
                'validators': []
            },
        }

    def get_reservation_on_my_vehicle(self, obj):
        user = self.context['request'].user
        return obj.is_car_owner(user)


class PhotoSerializer(serializers.ModelSerializer):
    """
    To create POST on http://127.0.0.1:8000/vehicles_sharing/photos/

    Body params:
    field: attached photo
    car: int

    to remove DELETE on http://127.0.0.1:8000/vehicles_sharing/photos/id/

    Body params:
    photo_id: int
    """

    # photo = serializers.FileField(required=True)

    class Meta:
        model = Photo
        fields = ('photo_id', 'photo', 'car', 'date_created')

    def get_car(self, obj):
        return obj.request.POST.car

    def get_date_created(self):
        return datetime.now()
