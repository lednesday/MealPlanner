from entry import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient
import datetime

'''
Create Database for tests
'''
client = MongoClient("localhost", 27017) # connect to engine.
db = client["Project2"] # create database
mealplanner = db['TestDatabase']
start_date = "2020-11-24"
end_date = "2020-11-26"
plan_name = "TestMealplan"
meals = [["Lunch", "Dinner"],["Breakfast", "Dinner"],["Lunch"]]
meal_plan = create_newplan(start_date, end_date , plan_name, meals)
insert_entry_mongo(meal_plan, mealplanner, "meal_plan")
print("######## After creation of a range of days ########")
print_database(mealplanner)
'''
Insert cooks's information and Dishes' information to its respective sections
'''
recipe_name = "Sandwich"
servings = 1
ingredients = [("Ham", 2, "slices"), ("Bread", 2, "slices"), ("Cheese", 2, "slices")]
directions = "You know how to make a sandwich, come on"
allergens = "wheat, cheese"
special_diets = ""
meal_plan = "TestMealplan"
create_insert_dish(recipe_name, servings, ingredients, directions, allergens, special_diets, meal_plan, mealplanner)
print("######## Adding one Sandwich recipe ########")
print_database(mealplanner)

recipe_name = "Eggs"
servings = 1
ingredients = [("Eggs", 2, "units"), ("Bread", 2, "slices"), ("Bacon", 2, "links")]
directions = "You know how to make a eggs, come on"
allergens = "wheat, ramen"
special_diets = "None"
meal_plan = "TestMealplan"
create_insert_dish(recipe_name, servings, ingredients, directions, allergens, special_diets, meal_plan, mealplanner)
print("######## Adding one eggs recipe ########")
print_database(mealplanner)
cook_name = "Jose"
cook_allergies = "Soy, Oil"
cook_restrictions = "Vegetarian"
cook_email = "alicia@testing.com"
create_insert_cook(cook_name, cook_allergies, cook_restrictions, cook_email, meal_plan, mealplanner)
print("######## Adding one Jose information ########")
print_database(mealplanner)
cook_name = "Antonio"
cook_allergies = "Wheat, Oil"
cook_restrictions = "Vegetarian"
cook_email = "vale@testing.com"
create_insert_cook(cook_name, cook_allergies, cook_restrictions, cook_email, meal_plan, mealplanner)
print("######## Adding one Jose information ########")
print_database(mealplanner)
'''
Adding dishes inside the mealplanner depending the day and meal
'''
add_dish_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Eggs")
add_dish_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Pasta")
add_dish_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Steak")
add_dish_mongo(mealplanner, plan_name, "2020-11-24", "Dinner", "Eggs")
add_dish_mongo(mealplanner, plan_name, "2020-11-24", "Dinner", "Soup")

add_dish_mongo(mealplanner, plan_name, "2020-11-25", "Breakfast", "Ramen")
add_dish_mongo(mealplanner, plan_name, "2020-11-25", "Breakfast", "Pasta")
add_dish_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Steak and eggs")
add_dish_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Eggs")
add_dish_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Rice")

add_dish_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Ramen Soup")
add_dish_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Rice")
add_dish_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Steak and rice")
add_dish_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Eggplant")
add_dish_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Sandwich")

print("######## Adding several dishes ########")
print_database(mealplanner)
'''
Adding cooks to the specific day and meals
'''
add_cook_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Antonio")
add_cook_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Maria")
add_cook_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Jose")
add_cook_mongo(mealplanner, plan_name, "2020-11-24", "Dinner", "Eric")
add_cook_mongo(mealplanner, plan_name, "2020-11-24", "Dinner", "Moriah")

add_cook_mongo(mealplanner, plan_name, "2020-11-25", "Breakfast", "Jonny")
add_cook_mongo(mealplanner, plan_name, "2020-11-25", "Breakfast", "Alicia")
add_cook_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Steph")
add_cook_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Tyler")
add_cook_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Amrit")

add_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Vanessa")
add_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Jose")
add_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Alicia")
add_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Mario")
add_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Maria")
print("######## Adding several cooks ########")
print_database(mealplanner)

delete_dish_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Eggs")
delete_dish_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Pasta")
delete_dish_mongo(mealplanner, plan_name, "2020-11-25", "Breakfast", "Ramen")
delete_dish_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Eggplant")
delete_dish_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Ramen Soup")
delete_dish_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Steak and eggs")
delete_dish_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Eggs")
delete_dish_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Rice")
print("######## Deleting several dishes ########")
print_database(mealplanner)

delete_cook_mongo(mealplanner, plan_name, "2020-11-24", "Lunch", "Jose")
delete_cook_mongo(mealplanner, plan_name, "2020-11-24", "Dinner", "Eric")
delete_cook_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Tyler")
delete_cook_mongo(mealplanner, plan_name, "2020-11-25", "Dinner", "Amrit")
delete_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Alicia")
delete_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Mario")
delete_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Alicia")
delete_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Mario")
delete_cook_mongo(mealplanner, plan_name, "2020-11-26", "Lunch", "Maria")
print("######## Deleting several cooks ########")
print_database(mealplanner)

delete_cook_database_mongo(mealplanner, plan_name, "Antonio")
delete_cook_database_mongo(mealplanner, plan_name, "Jose")


print("######## Deleting several cooks (full info)########")
print_database(mealplanner)

delete_dish_database_mongo(mealplanner, plan_name, "Eggs")


print("######## Deleting dishes from database (full recipes) ########")
print_database(mealplanner)

remove_plan(mealplanner, plan_name)
print("######## Deleting a mealplan (should print empty) ########")
print_database(mealplanner)

mealplanner.drop()
