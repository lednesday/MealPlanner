import pymongo # modules
from pymongo import MongoClient

client = MongoClient("localhost", 27017) # connect to engine.
client.drop_database("antonio_test")

db = client["antonio_test"] # create database
mealplanner = db.mealplanner # create

'''
FUNCTIONS

Diverse functions added that will add, modify and delete days and entries.
No more classes, everything is done exclusively with mongodb.
It should be not that difficult to extend to add recipes and cooks information
'''
#add new day
def new_day(collection, date: str):
    collection.insert_one({"date": date, "Meals": {}})

#add meals (breakfast, lunch, dinner)
def add_meals(collection, date: str, meals: str):
    collection.update_one({"date":date}, {'$set': {"Meals."+meals:{"dishes":[], "cooks":[]}}})

#add dish (in a date, meals represent in what meals the dish will go)
def add_dish(collection, date: str, meals: str, dish: str):
    collection.update_one({"date":date}, {'$push': {"Meals."+meals+".dishes": dish}})

#add dish (in a date, meals represent in what meals the cook will work)
def add_cook(collection, date: str, meal: str, cook: str):
    collection.update_one({"date":date}, {'$push': {"Meals."+meal+".cooks": cook}})

def retrieve_data_dishes(collection, date: str, meal: str):
    result = collection.find({"date":date}) #
    return result[0]["Meals"][meal]["dishes"]

def retrieve_data_cooks(collection, date: str, meal: str):
    result = collection.find({"date":date}) #
    return result[0]["Meals"][meal]["cooks"]

def retrieve_meals(collection, date: str):
    result = collection.find({"date":date}) #
    list = []
    for i in result[0]["Meals"]:
        list.append(i)
    return list

def delete_entry_mongo(collection, date_delete: str):
    myquery = { "date": date_delete }
    collection.delete_one(myquery)

def delete_dish(collection, date: str, meal: str, dish_delete:str):
    collection.update_one({"date":date}, { "$pull": { "Meals." + meal + ".dishes" : dish_delete }})

def delete_cook(collection, date: str, meal: str, cook_delete:str):
    collection.update_one({"date":date}, { "$pull": { "Meals." + meal + ".cooks" : cook_delete }})

def print_collection(col):
    for day in col.find():
        print(day)
        print()

'''
TESTING

Testing adding new days and filling it up with meals and dishes.
No using classes.
It can be extended to add more specific data.

People working in flask should suggest what kind of inputs and outputs would be good to have to communicate Flask with Mongodb. (i.e input a list?, a variable?. Return a list? a variable? a dict?)

'''

#DAY 1
day1 = "11-11-20"
new_day(mealplanner,day1)
meal1 ="Breakfast"
add_meals(mealplanner,day1,meal1)
add_dish(mealplanner, day1 , meal1, "Soup")
add_dish(mealplanner, day1 , meal1, "Lemon")
add_dish(mealplanner, day1 , meal1, "Tomato")
add_dish(mealplanner, day1 , meal1, "Egg")
add_cook(mealplanner, day1, meal1,"Antonio")
add_cook(mealplanner, day1, meal1,"Silvia")

meal1 = "Lunch"
add_meals(mealplanner,day1,meal1)
add_dish(mealplanner, day1 , meal1, "Steak")
add_dish(mealplanner, day1 , meal1, "Fish")
add_dish(mealplanner, day1 , meal1, "Lemon")
add_dish(mealplanner, day1 , meal1, "Eggs and potato")
add_cook(mealplanner, day1 , meal1, "Sara")
add_cook(mealplanner, day1 , meal1, "Camila")

meal1 = "Dinner"
add_meals(mealplanner,day1,meal1)
add_dish(mealplanner, day1 , meal1, "Past")
add_dish(mealplanner, day1 , meal1, "Fish Soup")
add_cook(mealplanner, day1 , meal1, "Jose")
add_cook(mealplanner, day1 , meal1, "Camila")
add_cook(mealplanner, day1 , meal1, "Pamela")

#DAY 2
day1 = "11-12-20"
new_day(mealplanner,day1)
meal1 ="Breakfast"
add_meals(mealplanner,day1,meal1)
add_dish(mealplanner, day1 , meal1, "Soup Fish")
add_dish(mealplanner, day1 , meal1, "Friend egg")
add_dish(mealplanner, day1 , meal1, "Tomato Pasta")
add_dish(mealplanner, day1 , meal1, "Egg soup")
add_cook(mealplanner, day1, meal1,"Mario")
add_cook(mealplanner, day1, meal1,"Silvia")

meal1 = "Lunch"
add_meals(mealplanner,day1,meal1)
add_dish(mealplanner, day1 , meal1, "Steak and potato")
add_dish(mealplanner, day1 , meal1, "FriedFish")
add_dish(mealplanner, day1 , meal1, "Eggs and potato")
add_cook(mealplanner, day1 , meal1, "Antonio")
add_cook(mealplanner, day1 , meal1, "Alejandro")

meal1 = "Dinner"
add_meals(mealplanner,day1,meal1)
add_dish(mealplanner, day1 , meal1, "Pasta")
add_dish(mealplanner, day1 , meal1, "Fish and pasta")
add_cook(mealplanner, day1 , meal1, "Mario")
add_cook(mealplanner, day1 , meal1, "Ana")

print("\n--- After adding 2 days:\n")
print_collection(mealplanner)

print("Different types of retrieves")


#testing retrieving information from database
print("Dishes for Lunch 11-12-20", retrieve_data_dishes(mealplanner, "11-12-20", "Lunch"))
print("Dishes for Breakfast 11-11-20", retrieve_data_dishes(mealplanner, "11-11-20", "Breakfast"))
print("Cooks for Breakfast 11-11-20", retrieve_data_cooks(mealplanner, "11-11-20", "Breakfast"))
print("List of meals in one day: ", retrieve_meals(mealplanner, "11-11-20"))

#retrieving just one element
lista_dishes = retrieve_data_dishes(mealplanner, "11-11-20", "Breakfast")

print(lista_dishes[1])

print("\n--- After delete: 11-11-20")

#delete entire day
delete_entry_mongo(mealplanner, "11-11-20")
#delete one dish from specific day and meal
delete_dish(mealplanner, "11-12-20", "Lunch", "FriedFish")

#delete one cook from specific day and meal
delete_cook(mealplanner, "11-12-20", "Lunch", "Alejandro")

print("--- After modify a dish and a cook in Lunch of 11-12-20\n")
print_collection(mealplanner)
