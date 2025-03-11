from django.db import models

class Recipe(models.Model):
    food_name = models.CharField(max_length=255, unique=True) 
    ingredients = models.TextField() 
    direction = models.TextField()  
    servings = models.CharField(max_length=50)  

    def __str__(self):
        return self.food_name
