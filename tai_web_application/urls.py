from django.contrib import admin
from django.urls import include
from django.urls import path

from vehicles_sharing import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles_sharing/', include(urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
