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
------------------------ DATABASE CLASSES -------------------------------
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
        if len(i) == 0:
            return 1
        for k in i:
            day_created[j].add_meal(Meal(k))
        mp.add_day(day_created[j])
        j += 1

    return mp



'''
gets names of cooks, if the name of mealplanner is provided for droplist
'''
def get_names_recipes(collection, mealplan:str):
    temp = []
    for i in return_dictionary_mongo(collection, mealplan)['recipes']:
        temp.append(i)
    return temp

'''
gets names of cooks, if the name of mealplanner is provided droplist
'''
def get_names_cooks(collection, mealplan:str):
    temp = []
    for i in return_dictionary_mongo(collection, mealplan)['cooks']:
        temp.append(i)
    return temp

'''
gets emails of cooks, if the name of mealplanner is provided
'''
def get_emails_cooks(collection, mealplan:str):
    temp = []
    for i in return_dictionary_mongo(collection, mealplan)['cooks'].values():
        temp.append(i['email'])
    return temp


'''
delete meal planner
'''
def remove_plan(collection, mealplan:str):
    collection.remove({"meal_plan":mealplan})


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
delete cook from meal_planner
'''
def delete_cook_database_mongo(collection, plan:str, cook:str): # enter and object (Day(), Dish(), Cook() or mealplan() and a type (str) (date, Name, Title)
    collection.update_one({"meal_plan":plan}, { '$unset': { "cooks."+cook:{} }})
'''
delete dish from meal_planner
'''
def delete_dish_database_mongo(collection, plan:str, dish:str): # enter and object (Day(), Dish(), Cook() or mealplan() and a type (str) (date, Name, Title)
    collection.update_one({"meal_plan":plan}, { '$unset': { "recipes."+dish:{} }})


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
returns an specific mealplanner (right now it returns cooks and their info)
'''
def return_dictionary_cooks(collection, meal_planner_name:str , cook:str):
    title = {}
    for i in collection.find({"meal_plan":meal_planner_name}):
        title = i

    return title['cooks'][cook]

'''
returns an specific mealplanner (right now it returns recipes and their info)
'''
def return_dictionary_recipes(collection, meal_planner_name:str , recipe:str):
    title = {}
    for i in collection.find({"meal_plan":meal_planner_name}):
        title = i

    return title['recipes'][recipe]

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
