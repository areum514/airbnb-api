from . import viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path


app_name = "rooms"

router = DefaultRouter()
router.register("",viewsets.RoomViewSet, basename='room')

urlpatterns = router.urls

# urlpatterns = [path("list",views.ListRoomView.as_view()),
# path("<int:pk>/",views.SeeRoomView.as_view())]
