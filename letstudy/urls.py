from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("base.urls")) # to direct every url to base's urls
]
