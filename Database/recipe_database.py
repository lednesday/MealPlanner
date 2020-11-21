
from entry import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient
from recipes_variables import * # for testing variables

client = MongoClient("localhost", 27017) # connect to engine.

db = client["Project2"] # create database
dish_database = db["Dish"] #create collection
'''
clean previous content of database (only when necessary, otherwise commented out.)
'''
dish_database.drop()

class Dish:
    '''
    Multiple dishes make up a meal, and each dish consists of its name, a list
    of ingredients, and a recipe.
    '''

    def __init__(self, name:str):
        '''
        creates day but it can add meals and cooks later. Date is required
        '''
        self.__name = name
        self.__ingredients = [] # list of ingredients
        self.__quantities = [] # List of ingredient quantities: indexes match.
        self.__units = [] # Units in which the quantities will be represented
        self.__recipe = ""
        self.__allergens = [] # list of allergens
        self.__restrictions = [] # Vegan, Gluten-Free, etc

    def get_index(self):
        '''
        get_index() is a method present in other classes like Day, Meal and Cook. It has the same name so we can use the same function with all the objects.
        '''
        return self.__name

    def add_recipe(self, recipe:str):
        '''
        Adds a recipe (in the appropriate format) to the dish
        '''
        self.__recipe = recipe

    def add_ingredients(self, ingredients: str):
        '''
        Adds an ingredient to the meal
        '''
        temp = ingredients.split(", ")
        for i in temp:
            self.__ingredients.append(i)

    def define_quantities(self, quantities:str):
        '''
        Defines the quantities of each meal ingredient
        '''
        temp = quantities.split(", ")
        for i in temp:
            self.__quantities.append(i)

    def define_units(self, units:str):
        '''
        Defines the quantities of each meal ingredient
        '''
        temp = units.split(", ")
        for i in temp:
            self.__units.append(i)

    '''
    Notes: My idea is that we have fields for ingredients and their quantities,
    as well as the recipe. Once inserted into their forms, each ingredient and 
    quantity field would be added by the add_ingredient and define_quantities 
    methods, which could be structured to already take in lists if that is easier
    to do on front-end. Recipe is just a string.

    For the moment, they are currently three strings: one for the ingredients and
    one for the quantities (separated by commas), and the one for the recipe.
    
    '''

    def add_allergens(self, allergens:str):
        '''
        Adds an allergen to the dish. is probably okay as a string.
        '''
        temp = allergens.split(", ")
        for i in temp:
            self.__allergens.append(i)

    def add_restrictions(self, restrictions:str):
        '''
        Adds a restriction to the dish. is probably okay as a string.
        '''
        temp = restrictions.split(", ")
        for i in temp:
            self.__restrictions.append(i)


    def get_dictionary(self):
        temp = {"title": self.__name,"recipe": self.__recipe, "ingredients": self.__ingredients, \
                "quantities":self.__quantities, "units":self.__units, "allergens":self.__allergens, \
                "restrictions":self.__restrictions}
        return temp


def create_insert_dish(name: str, recipe:str, ingredients:str, quantities:str, units:str, allergens:str, restrictions:str, collection):
    temp = Dish(name)
    temp.add_recipe(recipe)
    temp.add_ingredients(ingredients)
    temp.define_quantities(quantities)
    temp.define_units(units)
    temp.add_allergens(allergens)
    temp.add_restrictions(restrictions)
    insert_entry_mongo(temp, collection, "title")

create_insert_dish("Hologram food", "Shine light from hologram projector onto surface", "Light", "???", "watts", "None", "None", dish_database)


#test adding some dises (variables are in recipes_variables.py)
'''
create_insert_dish("Blistered Green Beans with Garlic", blistered_green, blistered_green_ingredients, dish_database)
create_insert_dish("Salt-and-Vinegar Rosti", salt_vinager, salt_vinager_ingredients, dish_database)
create_insert_dish("Teriyaki Chicken", teriyaki, teriyaki_ingredients, dish_database)
create_insert_dish("Green beans casserole", green_beans_casserole, green_beans_casserole_ingredients, dish_database)
create_insert_dish("Slow cooker smash potatos", Slow_cooker_smash_potatos, Slow_cooker_smash_potatos_ingredients, dish_database)
create_insert_dish("Keto Breakfast Sandwiches", Keto_Breakfast_Sandwiches, Keto_Breakfast_Sandwiches_ingredients, dish_database)
create_insert_dish("BBQ Cheeseburger Onion", BBQ_Cheeseburger_Onion, BBQ_Cheeseburger_Onion_ingredients, dish_database)
create_insert_dish("Slow Cooker Pork Shoulder", Slow_Cooker_Pork_Shoulder, Slow_Cooker_Pork_Shoulder_ingredients, dish_database)
create_insert_dish("Slow Cooker Chicken", Slow_Cooker_Chicken, Slow_Cooker_Chicken_ingredients, dish_database)
'''

print_database(dish_database)

'''
Get dates as lists
'''
for i in retrieve_data_index_list(dish_database, "title"):
    print(i)
