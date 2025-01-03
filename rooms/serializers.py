from rest_framework import serializers
from .models import House, Room, Wall


class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    walls = WallSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'
