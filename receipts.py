#! /urs/bin/env python3

import requests


def show_title():
    print("My Recipe Program")
    print()


def show_menu():
    print("COMMAND MENU")
    print("1 - List all categories")
    print("2 - List all meals for categories")
    print("3 - Search all meals by name")
    print("4 - Get a random meal")
    print("5 - List all areas")
    print("6 - List all meals for an area")
    print("7 - Display menu")
    print("0 - Exit the application")
    print()


def list_categories():
    # This method displays the list of categories to screen

    categories = requests.get_categories()

    if categories is not None:
        print("CATEGORIES")
        for i in range(len(categories)):
            category = categories[i]
            print("  " + category.get_category())
        print()
    else:
        print("Technical difficulties, please try again later.")
        print()


def list_meals_by_category():
    # This method displays the list of meals to screen

    lookup_category = input("Enter a category: ")
    print()

    categories = requests.get_categories()

    # Get the user menu selection
    if categories is not None:
        found = False

        for i in range(len(categories)):
            category = categories[i]
            if category.get_category().lower() == lookup_category.lower():
                found = True
                break

        if found:
            meals = requests.get_meals_by_category(lookup_category)
            if meals is not None:
                display_meals(lookup_category, meals)
            else:
                print("Technical difficulties, please try again later.")
                print()
        else:
            print("Invalid category, please try again.")

    else:
        print("Technical difficulties, please try again later.")
        print()


def search_meal_by_name():
    """
        This method is used to get a meals name from the user and
        make the call to get the meal from the site
    """

    lookup_meal = input("Enter Meal Name: ")

    meal = requests.get_meal_by_name(lookup_meal)
    if meal:
        display_meal(lookup_meal, meal)
    else:
        print("A recipe for this meal was not found.\n")


def display_meal(title, meal):
    # This method is used to display the meal information to screen
    print(title.upper(), "MEALS")
    print(meal)
    print()


def display_meals(title, meals):
    print(title.upper(), "MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print("  " + meal.get_meal_name())
    print()


def main():

    show_title()
    show_menu()

    while True:
        command = input("What would you like to do? ")
        print()

        if command == "1":
            list_categories()
        elif command == "2":
            list_meals_by_category()
        elif command == "3":
            search_meal_by_name()
        elif command == "0":
            print("Goodbye!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
