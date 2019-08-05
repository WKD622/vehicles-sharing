from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

from vehicles_sharing import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles_sharing/', include(urls)),
    path('api-token-auth/', obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
