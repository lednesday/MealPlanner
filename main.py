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
#First, create one day
day_one = create_day("10-10-20")

'''
Then we add the meals we want for that day
ENTRIES FOR BREAKFAST
'''
cooks = ["Antonio", "Milagros", "Jose", "Vanessa"]
dishes = ["Eggs", "Pasta", "Coffee", "Bloody Mary"]
#add breakfast Meal object to Day Object
add_meal_to_day(day_one, "Breakfast", cooks, dishes)


#ENTRIES FOR LUNCH for first day
cooks = ["Silvia", "Lisa", "Mario", "Alejandra","Antonio", "Rhian"]
dishes = ["Eggs soup", "Green Pasta", "Coffee and milk", "Steak"]
#add lunch Meal Object to Day Object
add_meal_to_day(day_one, "Lunch", cooks, dishes)

#Entries FOR DINNER for first day
cooks = ["Aaron", "Marce", "Homer", "Bart", "Lisa"]
dishes = ["Mushroom soup", "Red Pasta", "Latte", "Steak and chips"]
#add dinner Meal Object to day Object
add_meal_to_day(day_one, "Dinner", cooks, dishes)

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

'''
this part will create second day
'''

day_two = create_day("11-10-20")
cooks = ["Alejandra", "Melissa", "Pamela", "Silvia","Antonio", "Rhian"]
dishes = ["Eggs devil", "Pho", "Gelato", "Steak and rice"]
#add lunch Meal Object to Day Object
add_meal_to_day(day_two, "Lunch", cooks, dishes)
insert_entry_mongo(day_two, mealplanner)
print("\nAfter the second insert.\n")
for day in mealplanner.find():
    print(day)
    print()


'''
# this part will create third day
'''

day_three = create_day("12-10-20")
cooks = ["Maria", "Melissa", "Germania", "Ursula","Antonio", "Amaranta"]
dishes = ["Kidney pie", "Pizza", "Gelato", "Pasta"]
#add lunch Meal Object to Day Object
add_meal_to_day(day_three, "Breakfast", cooks, dishes)

cooks = ["Maria", "Antonio", "Amaranta"]
dishes = ["Apple pie", "Soup", "Gelato", "Potato Salad"]
#add lunch Meal Object to Day Object
add_meal_to_day(day_three, "Dinner", cooks, dishes)

insert_entry_mongo(day_three, mealplanner)

'''
# modify cooks and dishes
# date_find is a string with the date we want to modify,
# cooks and dishes are new lists with new info.
'''

date_find = "10-10-20"
cooks = ["NANA","TOTO","LIMA","LIMON"]
modify_cooks(mealplanner, date_find, "Lunch", cooks)
dishes = ["PIZZA","PIZZA", "PIZZA","PIZZA"]
modify_dishes(mealplanner, "11-10-20", "Lunch", dishes)

print("\nAfter the Third insert and modify  \n")
for day in mealplanner.find():
    print(day)
    print()

print("Delete second day\n")

#example to delete, first search (in this case a date)
#then delete from function
delete_entry_mongo(mealplanner, date_find)
for day in mealplanner.find():
    print(day)
    print()

print("List retrieve from the database")
query = retrieve_data(mealplanner, "12-10-20", "Meals")

for i in query:
    print(i)

client.close()
