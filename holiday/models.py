from django.db import models

# Create your models here.

class Holidays(models.Model):
    photo = models.FilePathField(path = '/images')
    description = models.TextField()
    price = models.FloatField()
    highlights = models.TextField()
    category = models.CharField(max_length = 15)
    days = models.IntegerField() 
