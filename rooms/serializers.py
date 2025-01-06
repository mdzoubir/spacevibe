from rest_framework import serializers
from .models import House, Room, Wall


class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ['id', 'start_x', 'start_y', 'end_x', 'end_y', 'height']


class RoomSerializer(serializers.ModelSerializer):
    walls = WallSerializer(many=True, read_only=True)  # Nested walls

    class Meta:
        model = Room
        fields = ['id', 'name', 'room_type', 'width', 'length', 'height', 'floor_number', 'walls']


class HouseSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)  # Related rooms

    class Meta:
        model = House
        fields = ['id', 'user', 'name', 'width', 'length', 'floors', 'created_at', 'rooms']
        read_only_fields = ['user', 'created_at']
