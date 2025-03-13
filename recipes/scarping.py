import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import json

# creating a User-Agent to avoid getting blocked 
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_recipe(url):
    """Scrape a single recipe from the given URL."""
    try:
        # Sending the  request
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        # Parsing to HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting the Structred data from the website
        script_tag = soup.find('script', {'type': 'application/ld+json'})
        if not script_tag:
            print(f" No structured data found for {url}")
            return None

        # Loading the extracted Json data
        data = json.loads(script_tag.string)

        # If data is a list, get the Recipe object
        if isinstance(data, list):
            recipe = next((item for item in data if "Recipe" in item.get("@type", [])), None)
        else:
            recipe = data if "Recipe" in data.get("@type", []) else None

        if not recipe:
            print(f" No recipe found in structured data for {url}")
            return None

        # Extracting Recipe Info in the website
        recipe_name = recipe.get("name", "No Title")
        prep_time = recipe.get("prepTime", "N/A")
        cook_time = recipe.get("cookTime", "N/A")
        total_time = recipe.get("totalTime", "N/A")
        serves = recipe.get("recipeYield", "N/A")
        freezing_time = recipe.get("freezingTime", "N/A")

        # Extracting Ingredients and directions
        ingredients = []
        for ingredient in recipe.get("recipeIngredient", []):
            if isinstance(ingredient, str):
                ingredients.append(ingredient.strip())

        ingredients_text = "\n".join(ingredients) if ingredients else "No Ingredients Found"

        directions = []
        for step in recipe.get("recipeInstructions", []):
            if isinstance(step, dict) and step.get("@type") == "HowToStep":
                directions.append(step.get("text", "").strip())

        directions_text = "\n".join(directions) if directions else "No Directions Found"

        # Storing the data in a dictionary
        recipe_data = {
            "Recipe Name": recipe_name,
            "Prep Time": prep_time,
            "Cook Time": cook_time,
            "Total Time": total_time,
            "Serves": serves,
            "Freezing Time": freezing_time,
            "Ingredients": ingredients_text,
            "Directions": directions_text
        }

        print(f"Scraped: {recipe_name}")
        return recipe_data

    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f" Failed to scrape {url}: {e}")
        return None

#Scrape multiple recipes and save them to a CSV

def scrape_multiple_recipes(urls):
    all_recipes = []

    for idx, url in enumerate(urls):
        print(f" Scraping {idx + 1}/{len(urls)}: {url}")
        recipe = scrape_recipe(url)

        if recipe:
            all_recipes.append(recipe)

        # delaying to prevent from getting blocked
        time.sleep(random.uniform(1, 3))

    # Saving the scraped data to CSV
    if all_recipes:
        df = pd.DataFrame(all_recipes)
        df.to_csv("scraped_recipes.csv", index=False)
        print(" Data saved to scraped_recipes.csv")
    else:
        print(" No recipes scraped.")


# these are the url which are scraped for the data
urls = [
    "https://www.seriouseats.com/banana-bread-pancakes-recipe-11691938",
    "https://www.seriouseats.com/bananas-foster-oatmeal-recipe-11689126",
    "https://www.seriouseats.com/maritozzi-recipe-11684437",
    "https://www.seriouseats.com/morning-glory-muffins-recipe-11683642",
    "https://www.seriouseats.com/churros-recipe-11680433",
    "https://www.seriouseats.com/savory-turmeric-oats-recipe-8772455",
    "https://www.seriouseats.com/rice-cooker-oatmeal-8766231",
    "https://www.seriouseats.com/yeasted-coffee-cake-recipe-8754688",
    "https://www.seriouseats.com/apple-pie-pancakes-recipe-8752129",
    "https://www.seriouseats.com/double-caramel-sticky-buns-recipe-8751530",
    "https://www.seriouseats.com/apple-pie-muffin-recipe-8749759",
    "https://www.seriouseats.com/colombian-arepas-de-huevo-recipe-11692079",
    "https://www.seriouseats.com/rice-cooker-oatmeal-8766231",
    "https://www.seriouseats.com/easy-overnight-oats-recipe-8664854",
    "https://www.seriouseats.com/microwave-granola-recipe-8778659",
    "https://www.seriouseats.com/easy-peanut-butter-banana-smoothie-recipe-8644710",
    "https://www.seriouseats.com/soft-scrambled-eggs-recipe",
    "https://www.seriouseats.com/avocado-smoothie-recipe-7375480",
    "https://www.seriouseats.com/breakfast-bars-recipe-8695308",
    "https://www.seriouseats.com/honey-butter-toast-recipe-8678981",
    "https://www.seriouseats.com/perfect-quick-easy-french-toast",
    "https://www.seriouseats.com/thick-and-fluffy-pancakes",
    "https://www.seriouseats.com/microwave-poached-eggs-recipe-8637441",
    "https://www.seriouseats.com/ful-mudammas-egyptian-breakfast-fava-beans-recipe",
    "https://www.seriouseats.com/nduja-scrambled-eggs",
    "https://www.seriouseats.com/florentine-omelette-spinach-and-cheese",
    "https://www.seriouseats.com/tortang-talong-eggplant-omelette-5189762",
    "https://www.seriouseats.com/western-omelette-with-bell-pepper-onion-ham-and-cheese",
    "https://www.seriouseats.com/classic-french-omelette-recipe",
    "https://www.seriouseats.com/bravetart-homemade-cinnamon-rolls-recipe",
    "https://www.seriouseats.com/savory-broccoli-and-cheese-galette",
    "https://www.seriouseats.com/french-style-soft-spoonable-scrambled-eggs-recipe",
    "https://www.seriouseats.com/bacon-cheese-and-kale-strata-5217605",
    "https://www.seriouseats.com/brunch-recipes-7557684",
    "https://www.seriouseats.com/basic-crepes-batter-recipe",
    "https://www.seriouseats.com/french-crepes-ham-cheese-eggs-recipe",
    "https://www.seriouseats.com/torrijas-caramelizadas-spanish-french-toast",
    "https://www.seriouseats.com/savory-green-curry-french-toast",
    "https://www.seriouseats.com/perfect-quick-easy-french-toast",
    "https://www.seriouseats.com/thick-and-fluffy-pancakes",
    "https://www.seriouseats.com/light-and-fluffy-pancakes-recipe",
    "https://www.seriouseats.com/buttermilk-vanilla-waffles-recipe",
    "https://www.seriouseats.com/shakshuka-north-african-shirred-eggs-tomato-pepper-recipe",
    "https://www.seriouseats.com/jamaican-banana-fritters-recipe-7498871",
    "https://www.seriouseats.com/cheese-danish-recipe-7487976",
    "https://www.seriouseats.com/youtiao-5207508",
    "https://www.seriouseats.com/jammy-fruit-bars",
    "https://www.seriouseats.com/jammy-fruit-bars",
    "https://www.seriouseats.com/daan-tat-hong-kong-style-egg-tart-5208534",
    "https://www.seriouseats.com/zucchini-tart-cream-cheese-mozzarella-5197867",
]

scrape_multiple_recipes(urls)
