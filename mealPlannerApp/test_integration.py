from entry import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient

client = MongoClient("localhost", 27017) # connect to engine.

'''
clean previous content of database.
because testing, if we don't drop the database everytime we test it, it will accumulate and make difficult to debug.
'''
client.drop_database("antonio_test")

db = client["antonio_test"] # create database
mealplanner = db.mealplanner # create

#create a day from "date"
day_one = create_day(date)

breakfast_dishes = [dish1_1, dish1_2]
lunch_dishes = [dish2_1, dish2_2]

#add meals to day_one
add_meal_to_day(day_one, meal1, cook1, breakfast_dishes)
add_meal_to_day(day_one, meal2, cook2, lunch_dishes)


'''
insert_entry_mongo will take a Day object and the database and will extract the dictionary from the object and insert it to the database
'''
result = insert_entry_mongo(day_one, mealplanner)

#print unique id of the recent document addes
print("Unique Id: {}\n".format(result))
print("\nAfter the first insert.\n")

#print entire content of the collection (table) it will print just one day
for day in mealplanner.find():
    print(day)
    print()

