from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from vehicles_sharing import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles_sharing/', include(urls)),
    path('api-token-auth/', obtain_auth_token),
]
