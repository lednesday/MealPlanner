from days_meals import *

#represent one day
day_one = Day("10-28-2020")

#each one represent
breakfast = Meal("Breakfast")
lunch = Meal("Lunch")
dinner = Meal("Dinner")

#adding dishes to breakfast meal. We should create an object "recipe" and add it to a meal
#adding names instead recipe objects
breakfast.add_recipe("Devil's eggs")
breakfast.add_recipe("Coffe")
breakfast.add_recipe("Latte")
breakfast.add_recipe("Moutain Muffin")

lunch.add_recipe("Soup")
lunch.add_recipe("Rice and beans")
lunch.add_recipe("Salmon and rice")
lunch.add_recipe("Pasta and tuna fish")

dinner.add_recipe("Clam Chowder")
dinner.add_recipe("Pasta and fish")
dinner.add_recipe("Potato Soup")

day_one.add_meal(breakfast)
day_one.add_meal(lunch)
day_one.add_meal(dinner)

print(day_one.get_meal()[0].get_recipe())#accesing through index for now, exploring using dict to acces through key.
