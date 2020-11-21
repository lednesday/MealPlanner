from entry import *
# from recipe_database import *
# from cook_database import *
# from recipe_database import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient
# from cook_variables import * #for testing variables
# from recipes_variables import * #for testing variables

client = MongoClient("localhost", 27017) # connect to engine.
'''
clean previous content of database
'''
# client.drop_database("cook")
db = client["Project2"] # create database
# cook_database = db["Dish"]
plan_database = db["Mealplanner"]

create_insert_cook("Dummy7", "Peanuts, fish", "Vegan", "dummytest@gmailcom", "hol", plan_database)

create_insert_dish("maria", "add water", "lemon , sugar", "1,2,3,4","m,d,s", "mam, aaa",'venga, mee', 'hol', plan_database)
print_database(plan_database)
