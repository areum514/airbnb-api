from . import views
from django.urls import path

app_name = "rooms"


urlpatterns = [path("list",views.rooms_view),
path("<int:pk>/",views.SeeRoomView.as_view())]
