from entry import *
import pandas as pd
from datetime import datetime

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

    for i in range_list:
        day_temp = Day(i) # first, create the day
        for j in list_meals:
            day_temp.add_meal(Meal(j    )) #then add all the meals that are in the list_meals
        mp.add_day(day_temp)

    return mp


def insert_entry_mongo(object, collection, type:str): # enter and object (Day(), Dish(), Cook() or mealplan() and a type (str) (date, Name, Title, meal_plan)
    if collection.count_documents({type: object.get_index() }, limit = 1) != 0:
        print("Record exists") #if the date already exists, it doesn't do anything
        return True
    else:
        temp = collection.insert_one(object.get_dictionary())
        return False #id returned (may need it later) returns 1 if exists and it fails to add.



'''
add dishes and cooks to mongodb
'''
def add_dish_mongo(collection, meal_plan_name:str, date_to_add: str, meal_to_add: str, dish: str): #add an extra dish when provided with a date and a meal.
    collection.update_one({"meal_plan":meal_plan_name}, {'$push': {"date."+date_to_add+".meals."+meal_to_add +".dishes": dish}})

def add_cook_mongo(collection, meal_plan_name:str, date_to_add: str, meal_to_add: str, cook: str): #add an extra dish when provided with a date and a meal.
    collection.update_one({"meal_plan":meal_plan_name}, {'$push': {"date."+date_to_add+".meals."+meal_to_add +".cooks": cook}})

def retrieve_data_index_list(collection, type): #return a list with index of tables ("date" for days, "title" for recipes and "name" for cooks)
    temp = []
    for i in collection.find():
        temp.append(i[type])
    return temp

def print_database(collection): #for debugging
    for day in collection.find():
        print(day)
        print()

def return_dictionary_mongo(collection, meal_planner_name:str ):
    # cur = mealplanner.find({"meal_plan":meal_planner_name})
    try:
        title = {}
        for i in collection.find({"meal_plan":meal_planner_name}):
            title = i
    except:
        print("Meal planner not found")

    return title






























'''
-------------- everything under this line is under revision!!! --------------------
'''
def search_date_in_mealplan(collection, mealplanner_name:str, date:list):
    for i in date:
        if collection.find( {"meal_plan" : mealplanner_name, "date." + i: {"$exists": True } } ).count() != 0:
            return True
    return False

'''
We create one day at the time
Input: date we want to add
output: Day object
'''
def create_day(date_event: str):
    return Day(date_event)

'''
It adds one meal at the time (breakfast, lunch or dinner)
one day can have many meals, one meal can have many dishes and many cooks
(we assume that all the cooks of one meal helps out with all the dishes of that meal)
input: day object, meal name, cooks list and dishes list.
output: None but it modify the Day Object
'''
def add_meal_to_day(day: Day, meal:str, cooks: list, dishes: list): #cooks and dishes are list.
    temp = Meal(meal)
    for i in cooks:
        temp.add_cook(i)
    for j in dishes:
        temp.add_dish(j)
    day.add_meal(temp)
'''
  ----------------------------------------------    MONGODB EXCLUSIVE FUNCTIONS    ----------------------------------------------
Mongodb functions: Modify and retrieve info from the database

extract the info inside the day object and convert it to dictionary, which is compatible to be storage into mongo. at last, it will insert it into the dictionary.

#COMPATIBLE with day(), dish(), cook()
'''
def insert_entry_mongo(object, collection, type:str): # enter and object (Day(), Dish(), Cook() and a type (date, Name, Title)
    if collection.count_documents({type: object.get_index() }, limit = 1) != 0:
        print("Record exists") #if the date already exists, it doesn't do anything
        temp = 1
    else:
        temp = collection.insert_one(object.get_dictionary())
    return temp #id returned (may need it later) returns 1 if exists


'''
deletes entry according to the date
input: mongo collection
output: delete by date
'''
def delete_day_entry_mongo(collection, date_to_delete: str): # delete one day in mongodb
    myquery = { "date": date_to_delete } # makes query to check record.
    collection.delete_one(myquery)

'''
add meals, dishes and cooks (in mongodb) -  EXCLUSIVE FOR DAY() MEALPLANNER
'''
def add_meals_mongo(collection, add_meal_to_date: str, meal: str): # add an extra meal in a day
    collection.update_one({"date":add_meal_to_date}, {'$set': {"Meals."+meal:{"dishes":[], "cooks":[]}}})

'''
delete a dish, cook, needs a date, a meal(breakfast, dinner, lunch, etc) and the dish we wish to delete  -  EXCLUSIVE FOR mongodb MEALPLANNER
'''
def delete_dish(collection, date: str, meal: str, dish_delete:str):
    collection.update_one({"date":date}, { "$pull": { "Meals." + meal + ".dishes" : dish_delete}})

def delete_cook(collection, date: str, meal: str, cook_delete:str):
    collection.update_one({"date":date}, { "$pull": { "Meals." + meal + ".cooks" : dish_delete}})

'''
Retrieve names, titles, dishes as a list to be use later (maybe for a drop down list?)
'''
def retrieve_data_meals(collection, date: str): #return the meals present in the database
    result = collection.find({"date":date}) #
    temp = []
    for i in result[0]['meals'].keys():
        temp.append(i)
    return temp
