from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Room
from  .serializers import RoomSerializer
# Create your views here.
@api_view(['GET'])
def list_rooms(request):
    rooms=Room.objects.all()
    serialized_rooms=RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)