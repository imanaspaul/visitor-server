from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('visitor.urls')),
    path("api/v1/", include('entrylog.urls'))
]
