from django.conf import settings
from django.db import models


class House(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    width = models.FloatField()
    length = models.FloatField()
    floors = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    ROOM_TYPES = [
        ('living', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('other', 'Other')
    ]

    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    width = models.FloatField()
    length = models.FloatField()
    height = models.FloatField()
    floor_number = models.IntegerField(default=1)


class Wall(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='walls')
    start_x = models.FloatField()
    start_y = models.FloatField()
    end_x = models.FloatField()
    end_y = models.FloatField()
    height = models.FloatField()