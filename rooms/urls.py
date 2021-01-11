from . import views
from django.urls import path

app_name = "rooms"

urlpatterns = [path("list",views.list_rooms)]
