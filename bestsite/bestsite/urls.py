from django.conf.urls.static import static
from django.urls import include
from django.contrib import admin
from django.urls import path
from cars.views import *

from bestsite import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('cars.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = pageNotFound