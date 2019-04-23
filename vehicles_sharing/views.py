from django.contrib.auth.models import User
from django_filters import filters
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Vehicle, Reservation
from .pom import PomMethods as pm
from .serializers import UserSerializer
from .serializers import VehicleSerializer
from .serializers import ReservationSerializer
from .pom import VehicleFilteringParams


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    # filter_backends = (filters.OrderingFilter,)
    # ordering_fields = ('price', 'power', 'production_year')

    def create(self, request, *args, **kwargs):
        user = pm.get_user_from_token(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner_id=user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        url_parameters = request.GET
        vehicles = Vehicle.objects.all()
        # pm.check_if_params_correct(self, url_parameters)
        for key, value in url_parameters.items():
            if key == VehicleFilteringParams.MIN_PRICE:
                vehicles = vehicles.filter(price__gte=value)
            elif key == VehicleFilteringParams.MAX_PRICE:
                vehicles = vehicles.filter(price__lte=value)
            elif key == VehicleFilteringParams.MIN_POWER:
                vehicles = vehicles.filter(power__gte=value)
            elif key == VehicleFilteringParams.MAX_POWER:
                vehicles = vehicles.filter(power__lte=value)
            elif key == VehicleFilteringParams.CITY:
                vehicles = vehicles.filter(city=value)
            elif key == VehicleFilteringParams.BRAND:
                vehicles = vehicles.filter(brand=value)
            elif key == VehicleFilteringParams.MODEL:
                vehicles = vehicles.filter(model=value)
            elif key == VehicleFilteringParams.MIN_PRODUCTION_YEAR:
                vehicles = vehicles.filter(production_year__gte=value)
            elif key == VehicleFilteringParams.MAX_PRODUCTION_YEAR:
                vehicles = vehicles.filter(production_year__lte=value)
            elif key == VehicleFilteringParams.MIN_CAPACITY:
                vehicles = vehicles.filter(capacity__gte=value)
            elif key == VehicleFilteringParams.MAX_CAPACITY:
                vehicles = vehicles.filter(capacity__lte=value)
            elif key == VehicleFilteringParams.DRIVE_TRAIN:
                vehicles = vehicles.filter(drive_train=value)

        serializer = self.get_serializer(vehicles, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def search(self, request, *args, **kwargs):
        found_entries = None
        if ('on' in request.GET) and request.GET['on'].strip():
            query_string = request.GET['on']
            entry_query = pm.get_query(query_string, ['brand', 'model'])
            found_entries = Vehicle.objects.filter(entry_query)

        serializer = self.get_serializer(found_entries, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def make_reservation(self, request, *args, **kwargs):
        vehicle = self.get_object()
        print(vehicle.id)
        owner = vehicle.owner_id
        client = pm.get_user_from_token(request)
        start_date = request.POST.get('start')
        end_date = request.POST.get('end')
        message = request.POST.get('message')
        reservation = {
            'client_id': client,
            'owner_id': owner,
            'car_id': vehicle,
            'start_date': start_date,
            'end_date': end_date,
            'active': True,
            'message': message
        }
        print(reservation)

        # Reservation.objects.create(**reservation)
        serializer = ReservationSerializer(data=reservation)
        serializer.is_valid()
        serializer.save()
        return Response("elo")


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, *args, **kwargs):
        new = self.get_object()
        return Response('eloszki' + new.id)
