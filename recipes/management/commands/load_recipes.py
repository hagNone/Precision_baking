import csv
from django.core.management.base import BaseCommand
from recipes.models import Recipe

class Command(BaseCommand):
    help = "Load recipes from CSV into the database"

    def handle(self, *args, **kwargs):
        with open(r"C:\Users\manoj\Downloads\Untitled spreadsheet - Sheet1 (1).csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  
            for row in reader:
                Recipe.objects.create(
                    food_name=row[1],     
                    ingredients=row[2],    
                    direction=row[3],     
                    servings=row[4]      
                )
        self.stdout.write(self.style.SUCCESS(" Recipes loaded successfully!"))
