from django.urls import path
from .views import get_recipe, recipe_page

urlpatterns = [
    path("", recipe_page, name="recipe_page"),  
    path("get_recipe/", get_recipe, name="get_recipe"),     
]
