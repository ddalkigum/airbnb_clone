from django.contrib import admin
from django.urls import path, include
from rooms.views import room_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("", include("rooms.urls", namespace="rooms")),
]
