from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import Room
from  .serializers import RoomSerializer, BigRoomSerializer
# Create your views here.

class ListRoomView(ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    
class SeeRoomView(RetrieveAPIView):
    queryset=Room.objects.all()
    serializer_class=BigRoomSerializer
