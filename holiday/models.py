from django.db import models
from makemyholiday.settings import STATIC_URL 
# Create your models here.

class Holidays(models.Model):
    name = models.CharField(max_length = 100)
    photo = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.FloatField()
    highlights = models.TextField()
    category = models.CharField(max_length = 15)
    days = models.IntegerField()

class Flight(models.Model):
    name = models.CharField(max_length=20)
    photo = models.CharField(max_length = 100)
    to = models.CharField(max_length=20)
    fro = models.CharField(max_length=20)
    depart_time = models.TimeField()
    arrival_time = models.TimeField() 
    days = models.CharField(max_length = 200)
    airlines = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length = 100)
    price_per_day = models.FloatField()
    address = models.TextField()
    category = models.CharField(max_length = 5) #ac /nonac
    amenities = models.TextField()