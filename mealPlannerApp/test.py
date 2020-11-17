from entry import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient

client = MongoClient("localhost", 27017) # connect to engine.

'''
clean previous content of database
'''
db = client["Project2"] # create database
mealplanner = db['Mealplanner']

start_date = "2020-10-1"
end_date = "2020-10-10"
meal_planner = "Trip"
meal_list = ["Breakfast", "Lunch", "Snacks", "Dinner"]

mealplan = create_newplan(start_date, end_date , meal_planner, meal_list)
# print(mealplan.get_dictionary())
insert_entry_mongo(mealplan, mealplanner, "meal_plan")

lista = date_range("2020-10-02", "2020-10-29")
print(lista)
search_date_in_mealplan(mealplanner, "Trip", lista)
