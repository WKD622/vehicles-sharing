from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.http import Http404
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .helpers import PomMethods as pm, VehicleFilteringParams
from .models import Vehicle, Reservation, Photo
from .serializers import ReservationSerializer, PhotoSerializer
from .serializers import UserSerializer
from .serializers import VehicleSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)

    @action(detail=False, methods=['POST'])
    def login(self, request, *args, **kwarg):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        # import pdb; pdb.set_trace();
        try:
            user = pm.get_user_from_username(username)
        except User.DoesNotExist:
            user = None

        if user and user.check_password(password):
            return Response(model_to_dict(pm.get_token_from_user_id(user.id)).get('key'))
        raise ValidationError("Invalid username or password")


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ('price', 'power', 'production_year',)
    ordering = ('id',)

    def create(self, request, *args, **kwargs):
        user = pm.get_user_from_token(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        if request.user == self.get_object().owner or request.user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            raise ValidationError("You are no allowed to edit this vehicle")

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().owner or request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You are no allowed to delete this vehicle")

    def list(self, request, *args, **kwargs):
        url_parameters = request.GET
        vehicles = Vehicle.objects

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

        if len(url_parameters) == 0 or len(url_parameters) == 1 and 'ordering' in url_parameters:
            vehicles = vehicles.all()

        page = self.paginate_queryset(vehicles)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

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

        new_reservation = {
            'client': pm.get_user_from_token(request),
            'owner': vehicle.owner,
            'car': vehicle,
            'start_date': request.POST.get('start_date'),
            'end_date': request.POST.get('end_date'),
            'active': False,
            'message': request.POST.get('message')
        }
        Reservation.objects.create(**new_reservation)
        new_reservation['client'] = model_to_dict(new_reservation['client'])
        new_reservation['owner'] = model_to_dict(new_reservation['owner'])
        new_reservation['car'] = model_to_dict(new_reservation['car'])

        serializer = ReservationSerializer(data=new_reservation)
        serializer.is_valid()
        return Response(serializer.initial_data)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(owner=self.request.user) | Reservation.objects.filter(
                client=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        if request.user == self.get_object().owner or request.user == self.get_object().client or request.user.is_superuser:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            raise ValidationError("You are no allowed to view this reservation")

    def update(self, request, *args, **kwargs):
        if request.user == self.get_object().owner or request.user.is_superuser or request.user == self.get_object().client and not self.get_object().active:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            raise ValidationError("You are no allowed to edit this reservation")

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().owner or request.user.is_superuser or request.user == self.get_object().client and not self.get_object().active:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You are no allowed to delete this reservation")

    @action(detail=True, methods=['POST'])
    def activate(self, request, *args, **kwargs):
        reservation = self.get_object()
        if reservation and self.request.user == reservation.owner or request.user.is_superuser:
            serializer = ReservationSerializer(reservation, data={'active': True}, partial=True)
            serializer.is_valid()
            self.perform_update(serializer)
            return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def deactivate(self, request, *args, **kwargs):
        reservation = self.get_object()
        if reservation and self.request.user == reservation.owner or request.user.is_superuser:
            serializer = ReservationSerializer(reservation, data={'active': False}, partial=True)
            serializer.is_valid()
            self.perform_update(serializer)
            return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def my_reservations(self, request, *args, **kwargs):
        user = pm.get_user_from_token(request)
        reservations = Reservation.objects.filter(client=user)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class DataViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_field = 'car'

    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):

        try:
            for k, v in kwargs.items():
                for id in v.split(','):
                    obj = get_object_or_404(Photo, pk=int(id))
                    obj.photo.delete()
                    self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_objects()
        serializer = PhotoSerializer(data=instance, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    def get_objects(self):

        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = queryset.filter(**filter_kwargs)

        return obj