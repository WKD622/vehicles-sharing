from django.urls import include, path
from rest_framework import routers

from vehicles_sharing import views
from vehicles_sharing.views import DataViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'photos', DataViewSet)

urlpatterns = [
    path('', include(router.urls))
]