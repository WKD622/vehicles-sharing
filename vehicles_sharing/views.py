from django.contrib.auth.models import User
from django_filters import filters
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
import re
from django.db.models import Q

from .models import Vehicle
from .serializers import UserSerializer
from .serializers import VehicleSerializer


class FilteringParams:
    MIN_PRICE = 'min_price'
    MAX_PRICE = 'max_price'
    MIN_POWER = 'min_power'
    MAX_POWER = 'max_power'
    CITY = 'city'
    BRAND = 'brand'
    MODEL = 'model'
    MIN_PRODUCTION_YEAR = 'min_production_year'
    MAX_PRODUCTION_YEAR = 'min_production_year'
    MIN_CAPACITY = 'min_capacity'
    MAX_CAPACITY = 'max_capacity'
    DRIVE_TRAIN = 'drive_train'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('price', 'power', 'production_year')

    @staticmethod
    def _get_user_from_token(request):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
        if token:
            user_id = Token.objects.get(key=token).user_id
            return User.objects.get(id=user_id)
        else:
            return None

    def _check_if_params_correct(self, params):
        """TODO"""
        pass

    def create(self, request, *args, **kwargs):
        user = self._get_user_from_token(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner_id=user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        url_parameters = request.GET
        vehicles = Vehicle.objects.all()
        self._check_if_params_correct(url_parameters)
        for key, value in url_parameters.items():
            if key == FilteringParams.MIN_PRICE:
                vehicles = vehicles.filter(price__gte=value)
            elif key == FilteringParams.MAX_PRICE:
                vehicles = vehicles.filter(price__lte=value)
            elif key == FilteringParams.MIN_POWER:
                vehicles = vehicles.filter(power__gte=value)
            elif key == FilteringParams.MAX_POWER:
                vehicles = vehicles.filter(power__lte=value)
            elif key == FilteringParams.CITY:
                vehicles = vehicles.filter(city=value)
            elif key == FilteringParams.BRAND:
                vehicles = vehicles.filter(brand=value)
            elif key == FilteringParams.MODEL:
                vehicles = vehicles.filter(model=value)
            elif key == FilteringParams.MIN_PRODUCTION_YEAR:
                vehicles = vehicles.filter(production_year__gte=value)
            elif key == FilteringParams.MAX_PRODUCTION_YEAR:
                vehicles = vehicles.filter(production_year__lte=value)
            elif key == FilteringParams.MIN_CAPACITY:
                vehicles = vehicles.filter(capacity__gte=value)
            elif key == FilteringParams.MAX_CAPACITY:
                vehicles = vehicles.filter(capacity__lte=value)
            elif key == FilteringParams.DRIVE_TRAIN:
                vehicles = vehicles.filter(drive_train=value)

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(vehicles, many=True)
        return Response(serializer.data)

    @staticmethod
    def _normalize_query(query_string,
                         findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                         normspace=re.compile(r'\s{2,}').sub):
        return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

    def _get_query(self, query_string, search_fields):
        query = None
        terms = self._normalize_query(query_string)
        for term in terms:
            or_query = None
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
        return query

    @action(detail=False, methods=['GET'])
    def search(self, request, *args, **kwargs):
        query_string = ''
        found_entries = None
        if ('on' in request.GET) and request.GET['on'].strip():
            query_string = request.GET['on']
            entry_query = self._get_query(query_string, ['brand', 'model'])
            found_entries = Vehicle.objects.filter(entry_query)

        serializer = self.get_serializer(found_entries, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def make_reservation(self, request, *args, **kwargs):
        """TODO"""
        pass


class ReservationViewSet(viewsets.ModelViewSet):
    pass
