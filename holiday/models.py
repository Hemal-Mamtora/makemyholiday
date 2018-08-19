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
