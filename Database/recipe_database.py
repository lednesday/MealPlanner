#23:35
from entry import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient
from recipes_variables import * # for testing variables

client = MongoClient("localhost", 27017) # connect to engine.

db = client["Project2"] # create database
recipe_database = db["Recipe"] #create collection
'''
clean previous content of database (only when necessary, otherwise commented out.)
'''
# recipe_database.drop()

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
        self.__recipe = ""

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

    def add_ingredients(self,ingredients: str):
        '''
        Adds an ingredient to the meal
        '''
        temp = ingredients.split(", ")
        for i in temp:
            self.__ingredients.append(i)

    def get_dictionary(self):
        temp = {"title": self.__name , "ingredients": self.__ingredients, "instructions":self.__recipe}
        return temp

def create_insert_recipe(name: str, recipe:str, ingredients: str, collection):
    temp = Dish(name)
    temp.add_recipe(recipe)
    temp.add_ingredients(ingredients)
    insert_entry_mongo(temp, collection, "title")

#test adding some recipes (variables are in recipes_variables.py)
create_insert_recipe("Blistered Green Beans with Garlic", blistered_green, ingredients, recipe_database)
create_insert_recipe("Salt-and-Vinegar Rosti", salt_vinager, salt_vinager_ingredients, recipe_database)
create_insert_recipe("Teriyaki Chicken", teriyaki, teriyaki_ingredients, recipe_database)
create_insert_recipe("Green beans casserole", green_beans_casserole, green_beans_casserole_ingredients, recipe_database)
create_insert_recipe("Slow cooker smash potatos", Slow_cooker_smash_potatos, Slow_cooker_smash_potatos_ingredients, recipe_database)
create_insert_recipe("Keto Breakfast Sandwiches", Keto_Breakfast_Sandwiches, Keto_Breakfast_Sandwiches_ingredients, recipe_database)
create_insert_recipe("BBQ Cheeseburger Onion", BBQ_Cheeseburger_Onion, BBQ_Cheeseburger_Onion_ingredients, recipe_database)
create_insert_recipe("Slow Cooker Pork Shoulder", Slow_Cooker_Pork_Shoulder, Slow_Cooker_Pork_Shoulder_ingredients, recipe_database)
create_insert_recipe("Slow Cooker Chicken", Slow_Cooker_Chicken, Slow_Cooker_Chicken_ingredients, recipe_database)

print_database(recipe_database)

'''
Get dates as lists
'''
for i in retrieve_data_index_list(recipe_database, "title"):
    print(i)
