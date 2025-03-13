from django.urls import path
from . import views 
from .views import get_recipe, recipe_page

urlpatterns = [
    path("", recipe_page, name="recipe_page"),  
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("get_recipe/", get_recipe, name="get_recipe"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),    
     path("reset_password/<str:token>/", views.reset_password, name="reset_password"),
]
