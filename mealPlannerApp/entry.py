'''
order: The system creates one day at the time. We fill it up with the date, the meals, the cooks and dishes.
'''

class Day:
    '''
    The program would create an array of days, each one containing
    '''
    def __init__(self, date:str ):
        '''
        creates day but it can add meals and cooks later. Date is required
        '''
        self.__date = date  # date (it cannot be changed, for now)
        self.__meal = []# list of meals objects

    def get_index(self):
        return self.__date# return date when the cook shift is happening

    def add_meal(self, meal): # meal is a Meal() object
        self.__meal.append(meal)
    def number_meals(self):
        return len(self.__meal)

    def get_dictionary(self):
        '''
        Formats all the info of the object into a json format ready to be inserted in mongodb
        '''

        result = {"date":self.get_index(),"meals":{}}

        for meal in self.__meal:
            result["meals"][meal.get_meal_name()] = \
            {"dishes":meal.get_dish_names(), "cooks":meal.get_cook_names()}

        return result


class Dish:
    '''
        Multiple dishes make up a meal, and each dish consists of its name, a list
    of ingredients, and a recipe.
    '''
    def __init__(self, name:str ):
        '''
        creates day but it can add meals and cooks later. Date is required
        '''
        self.__name = name
        self.__ingredients = [] # list of ingredients
        self.__recipe = "Placeholder for recipe"

    def add_recipe(recipe:str):
        '''
        Adds a recipe (in the appropriate format) to the dish
        '''
        self.__recipe = recipe

    def add_ingredient(ingredient:str):
        '''
        Adds an ingredient to the meal
        '''
        self.__ingredient.append(ingredient)

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__dish

    def print_recipe(self):
        print(self.__recipe) # May change depending on recipe format


class Cook:
    '''
    A cook is a person who will cook the meal. Each meal has one or more
    assigned cooks.
    '''

    def __init__(self, name:str):
        '''
        creates day but it can add meals and cooks later. Date is required
        '''
        self.__name = name # Cook's name
        self.__extra = [] # Cook's name


    def get_name(self):
        return self.__name

    def add_extra(self, info: str):
        '''
        add random info from cook (i.e. allergies, if prefer not to cook meat, etc)
        For now, it will add the info as a lidst of strings, one by one
        '''
        self.__extra.append(info) #


class Meal:
    '''
    "meal" is string that describes its (breakfast, lunch, dinner, etc)
    Each meal contains a list of dishes and cooks.
    '''
    def __init__(self, name: str):
        self.__name = name # string (breakfast, lunch, dinner)
        self.__dishes = [] # Dish objects
        self.__cooks = [] # Cook objects
    '''
    dishes an object (recipe object contain name, ingredients, allergies and instructions), meanwhile, string.
    '''
    def add_dish(self, dish:Dish):
        self.__dishes.append(dish) # "recipe" should have an attribute for allergies

    def add_cook(self, new_cook:Cook):
        self.__cooks.append(new_cook)# add cook per meal. There is different meals through the day but it can be different cooks

    def get_dishes(self):
        return self.__dishes

    def get_cooks(self):
        return self.__cooks

    def get_meal_name(self):
        return self.__name

    def get_dish_names(self):
        dish_names = []
        for dish in self.__dishes:
            dish_names.append(dish.get_name())

        return dish_names

    def get_cook_names(self):
        cook_names = []
        for cook in self.__cooks:
            cook_names.append(cook.get_name())

        return cook_names
