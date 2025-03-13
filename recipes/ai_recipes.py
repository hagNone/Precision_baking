import google.generativeai as genai
from recipes.models import Recipe

genai.configure(api_key="AIzaSyBjB_TNG1aCJvW8vbfXBLk7QON2cu1NUq0")

def fetch_recipe(user_input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Extract only the food name from this: '{user_input}'")#gets the food name from the given query
    food_name = response.text.strip()

   #filter the only food name in the databse with help of gemini model which gave the keyword to search
    recipe = Recipe.objects.filter(food_name__icontains=food_name).first()

    if not recipe:
        return f"Oops! I couldn't find a recipe for '{food_name}'. But hey, I can suggest some other amazing recipes! What are you in the mood for? 🍽️"

    #Prompting the model so it could respond in more human and interactive way
    interactive_prompt = f"""
    You're a fun and friendly AI assistant helping users cook delicious meals! 🎉

    A user is asking for the **{recipe.food_name}** recipe.
    Here's the structured data:

    - **Prep Time:** {recipe.prep_time}
    - **Cook Time:** {recipe.cook_time}
    - **Total Time:** {recipe.total_time}
    - **Serves:** {recipe.serves}
    - **Freezing Time:** {recipe.freezing_time}

    - **Ingredients:** {recipe.ingredients}
    - **Directions:** {recipe.directions}

    Format the response in a **fun, engaging, and conversational way**. Add emojis, a casual tone, and helpful tips where possible.
    """

    
    final_response = model.generate_content(interactive_prompt)

    return final_response.text.strip()
