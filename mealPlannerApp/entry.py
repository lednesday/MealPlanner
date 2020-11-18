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
        self.__meals = []# list of meals objects

    def get_index(self):
        return self.__date # return date when the cook shift is happening

    def add_meal(self, meal): # meal is a Meal() object
        self.__meals.append(meal)

    def get_meals(self):
        return self.__meals

    def get_dictionary(self):
        '''
        Formats all the info of the object into a json format ready to be inserted in mongodb
        '''

        result = {"meal_plan":self.get_index(), "date":{}}

        for day in self.__days:

            result["date"][day.get_index()] = {"meals":{}}

            for meal in day.get_meals():
                result["date"][day.get_index()]["meals"][meal.get_meal_name()] = {"dishes":meal.get_dishes(), "cooks":meal.get_cooks()}


        return result

class MealPlan:
    '''
    This is a MealPlan object, which contains the meal plan. It is made
    up of a name and a list of days.
    '''
    def __init__(self, name:str):
        '''
        creates day but it can add meals and cooks later. Date is required
        '''
        self.__name = name  # Name of the mealplan
        self.__days = [] # list of meals objects

    def get_index(self):
        return self.__name

    def add_day(self, day:Day):
        self.__days.append(day)

    def get_dictionary(self):
        '''
        Formats all the info of the object into a json format ready to be inserted in mongodb
        '''

        result = {"meal_plan":self.get_index(), "date":{}}

        for day in self.__days:
            result["date"][day.get_index()] = {"meals":{}}

            for meal in day.get_meals():
                result["date"][day.get_index()]["meals"][meal.get_meal_name()] = {"dishes":meal.get_dishes(), "cooks":meal.get_cooks()}

        return result


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
    def add_dish(self, dish:str ):
        self.__dishes.append(dish) # "recipe" should have an attribute for allergies

    def add_cook(self, new_cook:str ):
        self.__cooks.append(new_cook)# add cook per meal. There is different meals through the day but it can be different cooks

    def get_dishes(self):
        return self.__dishes

    def get_cooks(self):
        return self.__cooks

    def get_meal_name(self):
        return self.__name

# class Dish:
#     '''
#     Multiple dishes make up a meal, and each dish consists of its name, a list
#     of ingredients, and a recipe.
#     '''
#
#     def __init__(self, name:str):
#         '''
#         creates day but it can add meals and cooks later. Date is required
#         '''
#         self.__name = name
#         self.__ingredients = [] # list of ingredients
#         self.__recipe = "Placeholder for recipe"
#
#     def add_recipe(recipe:str):
#         '''
#         Adds a recipe (in the appropriate format) to the dish
#         '''
#         self.__recipe = recipe
#
#     def add_ingredient(ingredient:str):
#         '''
#         Adds an ingredient to the meal
#         '''
#         self.__ingredient.append(ingredient)
#
#     def get_name(self):
#         return self.__name
#
#     def get_ingredients(self):
#         return self.__dish
#
#     def print_recipe(self):
#         print(self.__recipe) # May change depending on recipe format


# class Cook:
    # '''
    # A cook is a person who will cook the meal. Each meal has one or more
    # assigned cooks.
    # '''
    #
    # def __init__(self, name:str):
    #     '''
    #     creates day but it can add meals and cooks later. Date is required
    #     '''
    #     self.__name = name # Cook's name
    #     self.__extra = [] # Cook's name
    #
    #
    # def get_name(self):
    #     return self.__name
    #
    # def add_extra(self, info: str):
    #     '''
    #     add random info from cook (i.e. allergies, if prefer not to cook meat, etc)
    #     For now, it will add the info as a lidst of strings, one by one
    #     '''
    #     self.__extra.append(info) #
