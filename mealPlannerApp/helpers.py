from entry import *
import pandas as pd
from datetime import datetime


'''
gets names of cooks, if the name of mealplanner is provided
'''
def get_names_recipes(collection, mealplan:str):
    temp = []
    for i in return_dictionary_mongo(collection, mealplan)['recipes']:
        temp.append(i)
    return temp

'''
gets names of cooks, if the name of mealplanner is provided
'''
def get_names_cooks(collection, mealplan:str):
    temp = []
    for i in return_dictionary_mongo(collection, mealplan)['cooks']:
        temp.append(i)
    return temp

def get_emails_cooks(collection, mealplan:str):
    temp = []
    for i in return_dictionary_mongo(collection, mealplan)['cooks'].values():
        temp.append(i['email'])
    return temp

'''
delete meal planner
'''
def remove_plan(collection, mealplan:str):
    print("hola")
    collection.remove({"meal_plan":mealplan})

'''
add cooks to db (CLASSES)
'''
def create_insert_cook(name: str, allergies:str, restrictions:str, email:str, mealplan:str, collection):
    temp = Cook(name)
    temp.add_allergies(allergies)
    temp.add_restrictions(restrictions)
    temp.add_email(email)
    insert_cook_mongo(temp, mealplan, collection)

'''
Add dish recipe to db (CLASSES)
'''

def create_insert_dish(name: str, servings:int, ingredients:list, recipe:str, allergens:str, restrictions:str, mealplan:str, collection):
    temp = Dish(name)
    temp.define_servings(servings)
    temp.add_ingredients(ingredients)
    temp.add_recipe(recipe)
    temp.add_allergens(allergens)
    temp.add_restrictions(restrictions)
    insert_recipe_mongo(temp, mealplan, collection)


'''
Date range functions: Provide a start date and a end date and it will return  a list of strings with all the dates.
'''
def date_range(start, end):
    temp_range = pd.date_range(start=start, end=end) # return a datetimeindex
    date_rng = temp_range.date

    lista = []
    for i in date_rng:
        lista.append(i.strftime('%Y-%m-%d'))

    return lista

'''
newplan functions following the format of the website

This function will create a place holder in the database from the start_date to the end_date, and it will add the meals (with empty list of cooks and dishes) that are selected in the front end.
'''

def create_newplan(start_date: str, end_date:str , name_plan:str, list_meals:list):
    mp = MealPlan(name_plan)

    range_list = date_range(start_date, end_date)

    day_created = []
    for i in range_list:
        day_created.append(Day(i))

    j = 0
    for i in list_meals:
        for k in i:
            day_created[j].add_meal(Meal(k))
        mp.add_day(day_created[j])
        j += 1

    return mp

'''
Main function to insert documents to meal_planner
'''
def insert_entry_mongo(object, collection, type:str): # enter and object (Day(), Dish(), Cook() or mealplan() and a type (str) (date, Name, Title, meal_plan)
    if collection.count_documents({type: object.get_index() }, limit = 1) != 0:
        print("Record exists") #if the date already exists, it doesn't do anything
        return True
    else:
        temp = collection.insert_one(object.get_dictionary())
        return False #id returned (may need it later) returns 1 if exists and it fails to add.

'''
insert cook to meal_planner
'''
def delete_cook_database_mongo(collection, plan:str, cook:str): # enter and object (Day(), Dish(), Cook() or mealplan() and a type (str) (date, Name, Title)
    collection.update_one({"meal_plan":plan}, {'$unset': {"cooks."+cook:{}}})   











'''
insert cook to meal_planner
'''
def insert_cook_mongo(object:Cook, plan:str, collection): # enter and object (Day(), Dish(), Cook() or mealplan() and a type (str) (date, Name, Title,
    collection.update_one({"meal_plan":plan}, {'$set': {"cooks."+object.get_index():object.get_dictionary()}})

'''
insert recipes to meal_planner
'''
def insert_recipe_mongo(object:Dish, plan:str, collection): # enter and object (Day(), Dish(), Cook() or mealplan() and a type (str) (date, Name, Title,
    collection.update_one({"meal_plan":plan}, {'$set': {"recipes."+object.get_index():object.get_dictionary()}})

'''
retrieve names from mealplanner(only mealplanner)
'''
def retrieve_data_index_list(collection): #return a list with index of tables ("date" for days, "title" for recipes and "name" for cooks)
    temp = []
    for i in collection.find():
        temp.append(i['meal_plan'])
    return temp

'''

print database  (debug)
'''
def print_database(collection): #for debugging
    for day in collection.find():
        print(day)
        print()

'''
returns an specific mealplanner
'''
def return_dictionary_cooks(collection, meal_planner_name:str , cook:str):
    title = {}
    for i in collection.find({"meal_plan":meal_planner_name}):
        title = i

    return title['cooks'][cook]

'''
returns an specific mealplanner
'''
def return_dictionary_mongo(collection, meal_planner_name:str ):
    title = {}
    for i in collection.find({"meal_plan":meal_planner_name}):
        title = i

    return title

'''
returns all the mealplanners
'''
def return_dictionary_mongo_all(collection):

    title = []
    for i in collection.find():
        title.append(i)

    return title

'''
create meal and add cooks and dishes. (CLASSES)
'''
# def create_meal_add(meal:str, cooks:list, dishes:list):
#     temp_meal = Meal(meal)
#     for i in cooks:
#         temp_meal.add_cook(i)
#     for i in dishes:
#         temp_meal.add_dish(i)
#
#     return temp_meal

# def create_cook_add(name: str, allergies:str, restrictions:str, email:str):
#     temp = Cook(name)
#     temp.add_allergies(allergies)
#     temp.add_restrictions(restrictions)
#     temp.add_email(email)
#     return temp


'''
Add meal. needs name of the planner and the date_event
'''
# def add_meals_day_mongo(collection, meal_planner:str, date: str, meal: Meal):
#     collection.update_one({"meal_plan":meal_planner}, {'$set': {'date.'+date+".meals":meal.get_dictionary_meal()}})

'''
Add cook to database, providing a plan name, a date, a meal and a cook
'''
def add_cook_mongo(collection, meal_plan_name:str, date_to_add: str, meal_to_add: str, cook: str):
    collection.update_one({"meal_plan":meal_plan_name}, {'$push': {'date.'+date_to_add+".meals."+meal_to_add+".cooks":cook}})



'''
Add dish to database, providing a plan name, a date, a meal and a cook
'''
def add_dish_mongo(collection, meal_plan_name:str, date_to_add: str, meal_to_add: str, dish: str):
    collection.update_one({"meal_plan":meal_plan_name}, {'$push': {'date.'+date_to_add+".meals."+meal_to_add+".dishes":dish}})
'''
Gets dishes, provide mealplan, day, meal
'''
def get_dishes_mongo(collection, meal_plan_name:str, date: str, meal: str):
    temp = return_dictionary_mongo(collection, meal_plan_name)
    result =temp['date'][date]['meals'][meal]['dishes']
    return result

'''
Gets cooks and dishes, provide mealplan, day, meal (para eliminar opciones seleccionadas
)
'''
def get_cooks_mongo(collection, meal_plan_name:str, date: str, meal: str):
    temp = return_dictionary_mongo(collection, meal_plan_name)
    result =temp['date'][date]['meals'][meal]['cooks']
    return result

def get_date_mongo(collection, meal_plan_name:str):
    temp = return_dictionary_mongo(collection, meal_plan_name)
    dates = []
    for key in temp['date']:
        dates.append(key)
    return dates

'''
delete one dish
'''
def delete_dish_mongo(collection, meal_plan_name:str, date: str, meal: str, dish:str):
    collection.update(
      { "meal_plan": meal_plan_name },
      { '$pull': { 'date.'+date+".meals."+meal+".dishes": dish} }
    );

def delete_cook_mongo(collection, meal_plan_name:str, date: str, meal: str, cook:str):
    collection.update(
      { "meal_plan": meal_plan_name },
      { '$pull': { 'date.'+date+".meals."+meal+".cooks": cook  } }
    );

'''
in progress
'''
def drop_list_cooks(collection, meal_plan_name):
    temp = return_dictionary_mongo(collection,meal_plan_name)['cooks']
    cooks = []
    for i in temp:
        cooks.append(i)

    return cooks

def drop_list_recipes(collection, meal_plan_name):
    temp = return_dictionary_mongo(collection,meal_plan_name)['recipes']
    cooks = []
    for i in temp:
        cooks.append(i)

    return cooks
































#
#
# '''
# -------------- everything under this line is under revision!!! --------------------
# '''
#
# '''
# create day and add meals
# function to add cooks and dishes
# '''
#
# # def create_day(date:str, meal:str, cooks:list, dishes:list ):
# #     temp_day = Day(date)
# #     temp_meal = Meal(meal)
# #
# #     for i in cooks:
# #         temp_meal.add_cook(i)
# #     for i in dishes:
# #         temp_meal.add_dish(i)
# #
# #     temp_day.add_meal(temp_meal)
# #
# #     return temp_day
#
#
# def add_dish_mongo(collection, meal_plan_name:str, date_to_add: str, meal_to_add: str, dish: str): #add an extra dish when provided with a date and a meal.
#     collection.update_one({"meal_plan":meal_plan_name}, {'$push': {"date."+date_to_add+".meals."+meal_to_add +".dishes": dish}})
#
# def add_cook_mongo(collection, meal_plan_name:str, date_to_add: str, meal_to_add: str, cook: str): #add an extra dish when provided with a date and a meal.
#     collection.update_one({"meal_plan":meal_plan_name}, {'$push': {"date."+date_to_add+".meals."+meal_to_add +".cooks": cook}})
#
# def search_date_in_mealplan(collection, mealplanner_name:str, date:list):
#     for i in date:
#         if collection.find( {"meal_plan" : mealplanner_name, "date." + i: {"$exists": True } } ).count() != 0:
#             return True
#     return False
#
# '''
# We create one day at the time
# Input: date we want to add
# output: Day object
# '''
# def create_day(date_event: str):
#     return Day(date_event)
# '''
# It adds one meal at the time (breakfast, lunch or dinner)
# one day can have many meals, one meal can have many dishes and many cooks
# (we assume that all the cooks of one meal helps out with all the dishes of that meal)
# input: day object, meal name, cooks list and dishes list.
# output: None but it modify the Day Object
# '''
# # def add_meal_to_day(day: Day, meal:str, cooks: list, dishes: list): #cooks and dishes are list.
# #     temp = Meal(meal)
# #     for i in cooks:
# #         temp.add_cook(i)
# #     for j in dishes:
# #         temp.add_dish(j)
# #     day.add_meal(temp)
# '''
#   ----------------------------------------------    MONGODB EXCLUSIVE FUNCTIONS    ----------------------------------------------
# Mongodb functions: Modify and retrieve info from the database
#
# extract the info inside the day object and convert it to dictionary, which is compatible to be storage into mongo. at last, it will insert it into the dictionary.
#
# #COMPATIBLE with day(), dish(), cook()
# '''
# def insert_entry_mongo(object, collection, type:str): # enter and object (Day(), Dish(), Cook() and a type (date, Name, Title)
#     if collection.count_documents({type: object.get_index() }, limit = 1) != 0:
#         print("Record exists") #if the date already exists, it doesn't do anything
#         temp = 1
#     else:
#         temp = collection.insert_one(object.get_dictionary())
#     return temp #id returned (may need it later) returns 1 if exists
#
# '''
# deletes entry according to the date
# input: mongo collection
# output: delete by date
# '''
# def delete_day_entry_mongo(collection, date_to_delete: str): # delete one day in mongodb
#     myquery = { "date": date_to_delete } # makes query to check record.
#     collection.delete_one(myquery)
#
# '''
# add meals, dishes and cooks (in mongodb) -  EXCLUSIVE FOR DAY() MEALPLANNER
# '''
# def add_meals_mongo(collection, add_meal_to_date: str, meal: str): # add an extra meal in a day
#     collection.update_one({"date":add_meal_to_date}, {'$set': {"Meals."+meal:{"dishes":[], "cooks":[]}}})
#
# '''
# delete a dish, cook, needs a date, a meal(breakfast, dinner, lunch, etc) and the dish we wish to delete  -  EXCLUSIVE FOR mongodb MEALPLANNER
# '''
# def delete_dish(collection, date: str, meal: str, dish_delete:str):
#     collection.update_one({"date":date}, { "$pull": { "Meals." + meal + ".dishes" : dish_delete}})
#
# def delete_cook(collection, date: str, meal: str, cook_delete:str):
#     collection.update_one({"date":date}, { "$pull": { "Meals." + meal + ".cooks" : dish_delete}})
#
# '''
# Retrieve names, titles, dishes as a list to be use later (maybe for a drop down list?)
# '''
# def retrieve_data_meals(collection, date: str): #return the meals present in the database
#     result = collection.find({"date":date}) #
#     temp = []
#     for i in result[0]['meals'].keys():
#         temp.append(i)
#     return temp
