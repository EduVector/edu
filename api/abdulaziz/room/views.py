from rest_framework import generics
from .serializers import RoomSerializer
from apps.structure.models import Room


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
