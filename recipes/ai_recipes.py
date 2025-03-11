import google.generativeai as genai
from recipes.models import Recipe

# Configure Gemini API
genai.configure(api_key="########################")

def fetch_recipe(user_input):
   
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Extract only the food name from this: '{user_input}'")
    food_name = response.text.strip()

    recipe = Recipe.objects.filter(food_name__icontains=food_name).first()

    if not recipe:
        return f"Oops! I couldn't find a recipe for '{food_name}'. But hey, I can suggest some other amazing recipes! What are you in the mood for? 🍽️"

    interactive_prompt = f"""
    You're a fun and friendly AI assistant helping users cook delicious meals! 🎉
    
    A user is asking for the **{recipe.food_name}** recipe. 
    Here's the structured data:
    
    - **Ingredients:** {recipe.ingredients}
    - **Directions:** {recipe.direction}
    - **Servings:** {recipe.servings}

    Format the response in a **fun, engaging, and conversational way**. Add emojis, casual tone, and helpful tips where possible.
    """

    final_response = model.generate_content(interactive_prompt)

    return final_response.text.strip()
