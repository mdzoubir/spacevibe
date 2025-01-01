from rest_framework import serializers

from furniture.models import FurnitureCategory, Furniture, FurniturePlacement
from rooms.serializers import RoomSerializer


class FurnitureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureCategory
        fields = ['id', 'name', 'description']


class FurnitureSerializer(serializers.ModelSerializer):
    category = FurnitureCategorySerializer(read_only=True)

    class Meta:
        model = Furniture
        fields = ['id', 'category', 'name', 'width', 'height', 'depth', 'image', 'price']


class FurniturePlacementSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    furniture = FurnitureSerializer(read_only=True)

    class Meta:
        model = FurniturePlacement
        fields = ['id', 'room', 'furniture', 'x_position', 'y_position', 'rotation', 'created_at']
