from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone
from rest_framework import serializers

from .models import Vehicle, Reservation
from .pom import Validators as validators


class Validators:
    only_letters = RegexValidator(regex=r'^[A-Z a-z]*', message='Only alphanumeric characters are allowed.')


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
    class Meta:
        model = Reservation
        fields = ('start_date', 'end_date', 'active', 'message', 'car_id')
