from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Vehicle
from .serializers import UserSerializer
from .serializers import VehicleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
        if token:
            user_id = Token.objects.get(key=token).user_id
            user = User.objects.get(id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner_id=user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
