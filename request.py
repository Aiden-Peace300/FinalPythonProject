from urllib import request, parse
import json

from objects import Category, Meal, Recipe


# Get a list of meal categories
def get_categories():

    # url for list of meals
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?c=list'
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)

    except (ValueError, KeyError, TypeError):
        return None

    return categories


# List all meals by category
def get_meals_by_category(category):

    # url for categories of meals
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=' + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])

            meals.append(meal)

    except (ValueError, KeyError, TypeError):
        return None

    return meals


# Search a meal by Name
def get_meal_by_name(meal):
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' + meal.replace(" ", "%20")
    f = request.urlopen(url)
    recipe = None

    try:
        data = json.loads(f.read().decode('utf-8'))
        print(data)
        instructions = data['meals'][0]['strInstructions']
        print(instructions)
        i = 1
        ingredients = []

        for ingredients[i] in data['meals'][0]:
            meal = Meal(ingredients[i]['strInstructions'])
            ingredients.append(meal)

        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])

            meals.append(meal)

        print(ingredients)

        # meal = Meal(name, recipe...
        for recipe_data in data['meals']:
            recipe = Recipe(recipe_data['idMeal'])

    except (ValueError, KeyError, TypeError):
        return None

    return recipe


'''
def get_meals_by_area(area):
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?a=' + area
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            area = Area(meal_data['strArea'])

            meals.append(area)

    except (ValueError, KeyError, TypeError):
        return None

    return meals
'''
