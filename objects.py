class Category:

    # constructor
    def __init__(self, category):
        self.__category = category

    # getter for category
    def get_category(self):
        return self.__category

    # setter for category
    def set_category(self, category):
        self.__category = category


class Meal:
    def __init__(self, meal_name):
        self.__meal_name = meal_name

    def get_meal_name(self):
        return self.__meal_name


class Recipe:
    def __init__(self, meal, category, instructions):
        self.__meal = meal
        self.__category = category
        self.__instructions = instructions

    def get_meal_name(self):
        return self.__meal

    def get_category(self):
        return self.__category

    def get_instructions(self):
        return self.__instructions


class Area:
    def __init__(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area
