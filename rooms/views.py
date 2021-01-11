from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Room
from  .serializers import RoomSerializer
# Create your views here.

class ListRoomView(ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    # def get(self,request):
    #     rooms=Room.objects.all()
    #     serializer=RoomSerializer(rooms, many=True)
    #     return Response(data=serializer.data)