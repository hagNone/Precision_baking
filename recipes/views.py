from django.shortcuts import render, redirect
from django.http import JsonResponse
from .ai_recipes import fetch_recipe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.contrib import messages

""" Main Home page """
@login_required
def recipe_page(request):
    return render(request, "index.html")

""" View Sign up Page """
@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect("login")
        return JsonResponse({"error": "User already exists"}, status=400)
    
    return render(request, "signup.html")

""" View for user_login page"""
@csrf_exempt
def user_login(request): 
    if request.method == "POST":  
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("recipe_page") 
        
        return JsonResponse({"error": "Invalid credentials!"}, status=401)
    
    return render(request, "login.html")

""" View for user logout """
@csrf_exempt
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

""" View for forgot_passsword page"""
reset_tokens = {}
@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        user = User.objects.filter(username=username).first()

        if user:
            # Generate and store token
            token = get_random_string(32)
            reset_tokens[token] = user.username

            # Redirect to reset password page with token
            return redirect(f"/reset_password/{token}/")

        return JsonResponse({"error": "User not Found!"}, status=400)

    return render(request, "forgot_password.html")

def reset_password(request, token):
    if token in reset_tokens:
        if request.method == 'POST':
            password = request.POST.get("password")
            user = User.objects.get(username=reset_tokens[token])
            user.set_password(password)
            user.save()
            del reset_tokens[token]
            messages.success(request, 'Password reset successful! Please log in.')
            return redirect('login')  # Redirect to login page

        # Render the reset password form
        return render(request, "reset_password.html", {"token": token})
    else:
        return JsonResponse({"error": "Invalid token!"}, status=400)

""" View for get_recipe """

@csrf_exempt
@login_required
def get_recipe(request):
    """Handle recipe fetching requests."""
    if request.method == "GET":
        user_input = request.GET.get("query", "").strip()

        if not user_input:
            return JsonResponse({"error": "No query provided!"}, status=400)

        try:
            # Example: Replace with actual logic to fetch recipe
            response = fetch_recipe(user_input)
            return JsonResponse({"response": response})
        except Exception as e:
            print("Error fetching recipe:", e)
            return JsonResponse({"error": "Internal server error"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

