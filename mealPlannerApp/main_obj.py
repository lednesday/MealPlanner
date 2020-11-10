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
mealplanner.drop()


'''
A form to add info would contain:
Add event ("DATE")
    Add Meal 1("Breakfast")
        Add Dish 1 -> Recipe and Ingredient
        Add Dish 2 -> Recipe and Ingredient
        Add Dish 3 -> Recipe and Ingredient

        Add Cook 1 -> Cook's name and extra info
        Add Cook 2 -> Cook's name and extra info
        Add Cook 3 -> Cook's name and extra info

    Add Meal 2("Lunch")
        Add Dish 1 -> Recipe and Ingredient
        Add Dish 2 -> Recipe and Ingredient
        Add Dish 3 -> Recipe and Ingredient

        Add Cook 1 -> Cook's name and extra info
        Add Cook 2 -> Cook's name and extra info
        Add Cook 3 -> Cook's name and extra info

    Add Meal 3("Dinner")
        Add Dish 1 -> Recipe and Ingredient
        Add Dish 2 -> Recipe and Ingredient
        Add Dish 3 -> Recipe and Ingredient

        Add Cook 1 -> Cook's name and extra info
        Add Cook 2 -> Cook's name and extra info
        Add Cook 3 -> Cook's name and extra info

First, create one day
'''
day = create_day("11-4-20")

'''
Then we add the meals we want for that day
ENTRIES FOR BREAKFAST

Pull info from the webform for the dishes and cooks.
'''

cook_1 = Cook("Antonio")#pull this info from the form
cook_2 = Cook("Milagros")
cook_3 = Cook("Jose")

dish_b1 = Dish("Eggs")
dish_b2 = Dish("Bacon")
dish_b3 = Dish("French Toast")

meal_name = "Breakfast"
cooks = [cook_1, cook_2, cook_3]
dishes = [dish_b1, dish_b2, dish_b3]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

'''
Second Meal of the day
'''

cook_1 = Cook("Jack")#pull this info from the form
cook_2 = Cook("Anna")
cook_3 = Cook("Jose")

dish_b1 = Dish("Chilaquiles")
dish_b2 = Dish("Bacon")
dish_b3 = Dish("Toast")

meal_name = "Lunch"
cooks = cooks = [cook_1, cook_2, cook_3]
dishes = [dish_b1, dish_b2, dish_b3]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

'''
Add info to the database
'''
print("\n--- Print First day\n")
print(day.get_index())

insert_entry_mongo(day, mealplanner, "date")
print_database(mealplanner) # print content so far


'''
Create day 2 and add 3 Meals with its cooks and dishes
'''
day = create_day("11-5-20")

cook_1 = Cook("Mario")#pull this info from the form
cook_2 = Cook("Zully")
cook_3 = Cook("Bart")

dish_b1 = Dish("Eggs and hot-dog")
dish_b2 = Dish("Pasta")
dish_b3 = Dish("Ceviche and Toasts")

meal_name = "Breakfast"
cooks = [cook_1, cook_2, cook_3]
dishes = [dish_b1, dish_b2, dish_b3]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

'''
Second Meal of the day
'''

cook_1 = Cook("Amanda")#pull this info from the form
cook_2 = Cook("Mario")
cook_3 = Cook("Jesse")

dish_b1 = Dish("Chichen Soup")
dish_b2 = Dish("Pork")
dish_b3 = Dish("Coffee")

meal_name = "Lunch"
cooks = [cook_1, cook_2, cook_3]
dishes = [dish_b1, dish_b2, dish_b3]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

'''
Third Meal of the day
'''
cook_1 = Cook("Jonny")#pull this info from the form
cook_2 = Cook("Moriah")
cook_3 = Cook("Lucy")

dish_b1 = Dish("Tofu")
dish_b2 = Dish("Fish")
dish_b3 = Dish("Lemonade")

meal_name = "Dinner"
cooks = cooks = [cook_1, cook_2, cook_3]
dishes = [dish_b1, dish_b2, dish_b3]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

print("\n--- Print 2nd day\n")
print(day.get_index())
insert_entry_mongo(day, mealplanner, "date")

print_database(mealplanner) # print content so far

'''
Create day 3 and add 3 Meals with its cooks and dishes
'''
day = create_day("11-6-20")

cook_1 = Cook("Antonio")#pull this info from the form
cook_2 = Cook("Zully")

dish_b1 = Dish("Eggs")
dish_b2 = Dish("Pizza")
dish_b3 = Dish("Club Sandwich")
dish_b4 = Dish("beef soup")

meal_name = "Breakfast"
cooks = [cook_1, cook_2]
dishes = [dish_b1, dish_b2, dish_b3, dish_b4]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

'''
Second Meal of the day
'''

cook_1 = Cook("Jackson")#pull this info from the form
cook_2 = Cook("Mario")
cook_3 = Cook("Jesse")
cook_4 = Cook("Maria")

dish_b1 = Dish("Bones Soup")
dish_b2 = Dish("Lemonade")
dish_b3 = Dish("Coffee")

meal_name = "Lunch"
cooks = [cook_1, cook_2, cook_4]
dishes = [dish_b1, dish_b2, dish_b3]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

'''
Third Meal of the day
'''

cook_1 = Cook("Lisa")#pull this info from the form
cook_2 = Cook("Homer")
cook_3 = Cook("Vanessa")

dish_b1 = Dish("Turkey sandwich")
dish_b2 = Dish("Milk and cocoa")

meal_name = "Dinner"
cooks = [cook_1, cook_2, cook_3]
dishes = [dish_b1, dish_b2]
#Then push it to the database
add_meal_to_day(day, meal_name, cooks, dishes)

print("\n--- Print 3nd day\n")
print(day.get_index())
insert_entry_mongo(day, mealplanner, "date")
print_database(mealplanner) # print content so far

'''
Delete entry from the 11-5-20
'''
print("\n--- Delete 2nd day\n")
date_delete ="11-5-20"
delete_day_entry_mongo(mealplanner, date_delete)
print_database(mealplanner) # print content so far

'''
Add one extra meal to the third date
'''
print("\n--- Add an extra meal to Third date")
date = "11-6-20"
meal = "Snack"
add_meals_mongo(mealplanner, date, meal)
print_database(mealplanner) # print content so far

'''
Add 2 extra meals into the recently "Snack" meal on 11-06-20
'''
print("\n--- Add 2 extra dishes to Third day, newly added Snack meal\n")
date = "11-6-20"
meal = "Snack"
dish = "Fried fish"
add_dish_mongo(mealplanner, date, meal, dish)
dish = "Oyster"
add_dish_mongo(mealplanner, date, meal, dish)
print_database(mealplanner) # print content so far

'''
Add 2 extra cooks into the recently "Snack" meal on 11-06-20
'''
print("\n--- Add 2 extra cooks to Third day, newly added Snack meal\n")
date = "11-6-20"
meal = "Snack"
cook = "Francisco"
add_cook_mongo(mealplanner, date, meal, cook)
cook = "John"
add_cook_mongo(mealplanner, date, meal, cook)
print_database(mealplanner) # print content so far

'''
Delete one dish from "11-4-20"
'''
print("\n--- Delete one dish (Bacon) on 'Breakfast' in the first day\n")
date = "11-4-20"
meal = "Breakfast"
dish_delete = "Bacon"
delete_dish(mealplanner, date, meal, dish_delete)
print_database(mealplanner) # print content so far

'''
Get dates as lists
'''
print("\n--- Print list of dates in the database as a list (Maybe can be used as a drop-down list) ---\n")
for i in retrieve_data_index_list(mealplanner, "date"):
    print(i)

print("\n--- Print list of meals in certain date in the database as a list (Maybe can be used as a drop-down list) ---\n")
for i in retrieve_data_meals(mealplanner, "11-4-20"):
    print(i)



client.close()
