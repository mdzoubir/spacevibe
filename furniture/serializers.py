from rest_framework import serializers

from furniture.models import FurnitureCategory, Furniture, FurniturePlacement
from rooms.serializers import RoomSerializer


class FurnitureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureCategory
        fields = '__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

class FurniturePlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurniturePlacement
        fields = '__all__'
