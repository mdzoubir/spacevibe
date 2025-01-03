from django.shortcuts import render
from rest_framework import viewsets

from furniture.models import FurnitureCategory, Furniture, FurniturePlacement
from furniture.serializers import FurnitureCategorySerializer, FurnitureSerializer, FurniturePlacementSerializer


# Create your views here.
class FurnitureCategoryViewSet(viewsets.ModelViewSet):
    queryset = FurnitureCategory.objects.all()
    serializer_class = FurnitureCategorySerializer


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class FurniturePlacementViewSet(viewsets.ModelViewSet):
    queryset = FurniturePlacement.objects.all()
    serializer_class = FurniturePlacementSerializer
