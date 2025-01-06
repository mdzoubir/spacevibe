from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import House, Room, Wall
from .serializers import HouseSerializer, RoomSerializer, WallSerializer

class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HouseSerializer

    def get_queryset(self):
        return House.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(house__user=self.request.user)

class WallViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WallSerializer
    queryset = Wall.objects.all()