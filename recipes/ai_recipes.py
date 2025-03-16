import google.generativeai as genai
from recipes.models import Recipe
import re


genai.configure(api_key="AIzaSyBjB_TNG1aCJvW8vbfXBLk7QON2cu1NUq0")

def clean_response(response_text):
    """Cleans the response by removing unwanted symbols and ensuring proper formatting."""
    cleaned_text = re.sub(r'\*+', '', response_text)  # Remove stars
    cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', cleaned_text)  # Remove non-ASCII (like emojis)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Clean extra spaces
    return cleaned_text

def fetch_recipe(user_input):
    """Fetches a recipe and generates a fun, human-like response."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # Extract the food name using Gemini
    response = model.generate_content(f"Extract only the food name from this: '{user_input}'")
    food_name = response.text.strip()
    
    # Search the database for the food name
    recipe = Recipe.objects.filter(food_name__icontains=food_name).first()

    if not recipe:
        return f"Oops! I couldn't find a recipe for '{food_name}'. But hey, I can suggest some other amazing recipes! What are you in the mood for? 🍽️"

    # Construct the prompt for Gemini to format the recipe nicely
    interactive_prompt = f"""
You're a fun and friendly AI assistant helping users cook delicious meals! 🎉

A user is asking for the **{recipe.food_name}** recipe.
Here’s the structured data:

- **Prep Time:** {recipe.prep_time}
continue from the next line
- **Cook Time:** {recipe.cook_time}
continue from the next line
- **Total Time:** {recipe.total_time}
continue from the next line
- **Serves:** {recipe.serves}
continue from the next line
- **Freezing Time:** {recipe.freezing_time}
continue from the next line

**INGREDIENTS:**  
{recipe.ingredients if recipe.ingredients else "No ingredients found!"}
continue from the next line
**DIRECTIONS:**  
{recipe.directions if recipe.directions else "No directions found!"}
continue from the next line

Format the response in a clean, article-like structure:  
- Start with a fun introduction.
- Separate ingredients and directions into distinct sections with clear headings.  
- Use line breaks between each step and ingredient.  
- Keep it engaging with a casual tone, and sprinkle in some emojis where it fits.  
"""


    # Get the final response from Gemini
    final_response = model.generate_content(interactive_prompt)
    
    # Clean the response for better readability
    cleaned_response = clean_response(final_response.text)

    return cleaned_response
