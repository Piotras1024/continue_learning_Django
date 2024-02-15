from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=0)
    room_number = models.IntegerField(default=0)


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = forei
    def __str__(self):
        return f"{self.title} start at {self.start_time} it will take {self.duration} at {self.date}"


# Create your models here.
