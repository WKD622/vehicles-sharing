from django.contrib.auth.models import User
from django_filters import filters
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Vehicle
from .serializers import UserSerializer
from .serializers import VehicleSerializer
from enum import Enum


class Sorting(Enum):
    HIGH_TO_LOW = "HIGH_TO_LOW"
    LOW_TO_HIGH = "LOW_TO_HIGH"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('price', 'power')

    @staticmethod
    def _get_user_from_token(request):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
        if token:
            user_id = Token.objects.get(key=token).user_id
            return User.objects.get(id=user_id)
        else:
            return None

    def create(self, request, *args, **kwargs):
        user = self._get_user_from_token(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner_id=user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def list(self, request, *args, **kwargs):
        # min_price = request.GET.get('min_price')
        # max_price = request.GET.get('max_price')
        # min_power = request.GET.get('min_power')
        # max_power = request.GET.get('max_power')
        # city = request.GET.get('city')
        # brand = request.GET.get('brand')
        # model = request.GET.get('model')
        # min_production_year = request.GET.get('min_production_year')
        # min_production_year = request.GET.get('min_production_year')
        # power = request.GET.get('power')
        # min_capacity = request.GET.get('min_capacity')
        # max_capacity = request.GET.get('max_capacity')
        # drive_train = request.GET.get('drive_train')
        #
        # for key, value in variables.items():
        #     if key == 'x' and value:
        #         models = models.filter(x=value)
        #     if key == 'y' and value:
        #         models = models.filter(y=value)
        #     if key == 'z' and value:
        #         models = models.filter(z=value)
        #
        # queryset = Vehicle.objects.all().filter(price__gte=min_price). \
        #     filter(price__lte=max_price)

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def make_reservation(self, request, *args, **kwargs):
        """TODO"""
        pass
