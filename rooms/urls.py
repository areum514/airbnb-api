from . import views
from django.urls import path

app_name = "rooms"


urlpatterns = [path("",views.RoomsView.as_view()),
path("search",views.serch_room),

path("<int:pk>/",views.RoomView.as_view())]
