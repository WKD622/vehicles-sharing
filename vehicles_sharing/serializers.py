from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from rest_framework import serializers
from django.utils import timezone

from .models import Vehicle, Reservation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    """
    TODO
    add drive_trains choices
    """
    price = serializers.IntegerField(min_value=0, max_value=3000000)
    production_year = serializers.IntegerField(min_value=1800, max_value=timezone.now().year + 2)
    description = serializers.CharField(max_length=10000)
    brand = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    drive_train = serializers.CharField(min_length=3, max_length=3)
    capacity = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    power = serializers.IntegerField(min_value=0, max_value=10000)
    city = serializers.CharField(max_length=50)
    street = serializers.CharField(max_length=50)

    class Meta:
        model = Vehicle
        fields = ('brand', 'model', 'price', 'production_year', 'description', 'drive_train', 'city', 'street', 'power',
                  'capacity')


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('start_date', 'end_date', 'active', 'message', 'car_id')
