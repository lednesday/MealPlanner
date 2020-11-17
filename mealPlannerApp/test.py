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

start_date = "2020-10-01"
end_date = "2020-10-03"
meal_planner = "New plan"
meal_list = ["Breakfast", "Lunch"]

mealplan = create_newplan(start_date, end_date , meal_planner, meal_list)
# print(mealplan.get_dictionary())
# insert_entry_mongo(mealplan, mealplanner, "meal_plan")
# day1 = "2020-10-01"
# add_dish_mongo(mealplanner, meal_planner, day1, "Breakfast", "Eggs")
# add_dish_mongo(mealplanner, meal_planner, day1, "Breakfast", "Pasta")
# add_dish_mongo(mealplanner, meal_planner, day1, "Lunch", "Banana")
# add_dish_mongo(mealplanner, meal_planner, day1, "Lunch", "Milk")
# add_cook_mongo(mealplanner, meal_planner, day1, "Breakfast", "Mario")
# add_cook_mongo(mealplanner, meal_planner, day1, "Lunch", "Pedro")
# day1 = "2020-10-02"
# add_dish_mongo(mealplanner, meal_planner, day1, "Breakfast", "Potato")
# add_dish_mongo(mealplanner, meal_planner, day1, "Breakfast", "Steak and Rice")
# add_dish_mongo(mealplanner, meal_planner, day1, "Lunch", "Egg and rice")
# add_dish_mongo(mealplanner, meal_planner, day1, "Lunch", "Coffee")
# add_cook_mongo(mealplanner, meal_planner, day1, "Breakfast", "Lindsay")
# add_cook_mongo(mealplanner, meal_planner, day1, "Lunch", "Maxine")
# day1 = "2020-10-03"
# add_dish_mongo(mealplanner, meal_planner, day1, "Breakfast", "Red pasta")
# add_dish_mongo(mealplanner, meal_planner, day1, "Breakfast", "Steak and Potato")
# add_dish_mongo(mealplanner, meal_planner, day1, "Lunch", "Soup")
# add_dish_mongo(mealplanner, meal_planner, day1, "Lunch", "Coffee")
# add_cook_mongo(mealplanner, meal_planner, day1, "Breakfast", "Bria")
# add_cook_mongo(mealplanner, meal_planner, day1, "Lunch", "Antonio")

x   = []
cur = mealplanner.find({"meal_plan":"New plan"})
for i in cur:
    print (i['meal_plan'])

for i in cur:
    print (i['meal_plan']['date']['2020-10-01'])

# print("\nPrint name\n")
# print(cur['meal_plan'])
# print("\nDate (contains other directories)\n")
# print(cur['date'])
# print("\nPrint first day in mealplanner. Breakfast\n")
# # print(cur['date']['2020-10-01'])
# print(cur['date']['2020-10-01']['meals']['Breakfast'])
# print("\nPrint first day in mealplanner. Lunch\n")
# print(cur['date']['2020-10-01']['meals']['Lunch'])





# print_database(mealplanner)
# def add_dish_mongo(collection, meal_plan_name:str, date_to_add: str, meal_to_add: str, dish: str): #add an extra dish when provided with a date and a meal.
