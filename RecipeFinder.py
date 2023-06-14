import requests

class RecipeFinder:
    def __init__(self, api_key):
        self.api_key = api_key

    def find_recipes(self, ingredient):
        url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredient}&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            if data:
                print(f"Recipes with {ingredient}:")
                for recipe in data:
                    recipe_name = recipe["title"]
                    recipe_id = recipe["id"]
                    print(f"- {recipe_name} (ID: {recipe_id})")
            else:
                print(f"No recipes found with {ingredient}.")
        else:
            print("Unable to retrieve recipe information.")

def main():
    api_key = "YOUR_API_KEY"
    ingredient = "chicken"

    finder = RecipeFinder(api_key)
    finder.find_recipes(ingredient)

if __name__ == "__main__":
    main()
