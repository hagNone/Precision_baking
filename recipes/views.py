from django.shortcuts import render
from django.http import JsonResponse
from .ai_recipes import fetch_recipe

def recipe_page(request):
    return render(request, "index.html") 

def get_recipe(request):
    if request.method == "GET":
        user_input = request.GET.get("query", "").strip()

        if not user_input:
            return JsonResponse({"error": "No query provided!"}, status=400)

        try:
            response = fetch_recipe(user_input) 
            return JsonResponse({"response": response})
        except Exception as e:
            print(" Error fetching recipe:", e)  
            return JsonResponse({"error": "Internal server error"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
