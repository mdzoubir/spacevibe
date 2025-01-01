from django.db import models

from rooms.models import Room


# Create your models here.
class FurnitureCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Furniture(models.Model):
    category = models.ForeignKey(FurnitureCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    image = models.ImageField(upload_to='furniture/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

class FurniturePlacement(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    x_position = models.FloatField()
    y_position = models.FloatField()
    rotation = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
