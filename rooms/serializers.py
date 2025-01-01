from rest_framework import serializers
from .models import House, Room, Wall
from users.serializers import UserSerializer

class HouseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = House
        fields = ['id', 'user', 'name', 'width', 'length', 'floors', 'created_at']


class RoomSerializer(serializers.ModelSerializer):
    house = HouseSerializer(read_only=True)  # Nested House serializer

    class Meta:
        model = Room
        fields = ['id', 'house', 'name', 'room_type', 'width', 'length', 'height', 'floor_number']


class WallSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)  # Nested Room serializer

    class Meta:
        model = Wall
        fields = ['id', 'room', 'start_x', 'start_y', 'end_x', 'end_y', 'height']
