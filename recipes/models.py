from django.db import models
from django.contrib.auth.models import User


"""
Create models for the database using python code because django supports Object to relational mapping

"""


#this model where it creates Recipe table and stores related columns
class Recipe(models.Model):
    food_name = models.CharField(max_length=255)
    prep_time = models.CharField(max_length=50, blank=True, null=True)
    cook_time = models.CharField(max_length=50, blank=True, null=True)
    total_time = models.CharField(max_length=50, blank=True, null=True)
    serves = models.CharField(max_length=50, blank=True, null=True)
    freezing_time = models.CharField(max_length=50, blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.food_name
