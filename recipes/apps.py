from django.apps import AppConfig
from .models import Recipe

class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    def ready(self):
        import Recipe.signals
