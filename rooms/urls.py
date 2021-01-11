from . import views
from django.urls import path

app_name = "rooms"

urlpatterns = [path("list",views.ListRoomView.as_view())]
