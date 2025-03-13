from django.core.management.base import BaseCommand
from recipes.models import Recipe
import pandas as pd

"""
This is where we create the function to load the data to the database or populate the database which is from the external source'
"""
class Command(BaseCommand):
    help = "Load recipes into the database"

    def handle(self, *args, **kwargs):
      
        df = pd.read_csv(r'C:\Users\manoj\precision_baking\recipes\scraped_recipes.csv')

        # here we Iterating through rows and save them to Data base
        for _, row in df.iterrows():
            Recipe.objects.create(
                food_name=row.get('Recipe Name', 'N/A'),
                prep_time=row.get('Prep Time', 'N/A'),
                cook_time=row.get('Cook Time', 'N/A'),
                total_time=row.get('Total Time', 'N/A'),
                serves=row.get('Serves', 'N/A'),
                freezing_time=row.get('Freezing Time', 'N/A'),
                ingredients=row.get('Ingredients', 'N/A'),
                directions=row.get('Directions', 'N/A'),
            )

        self.stdout.write(self.style.SUCCESS("Recipes loaded successfully!"))