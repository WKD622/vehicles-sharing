from django.urls import include, path
from rest_framework import routers

from vehicles_sharing import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'vehicles', views.EmployeeViewSet)
router.register(r'rentals', views.IncomeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
