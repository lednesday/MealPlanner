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
# mealplanner.drop()
list_recipe = db['recipe']

"""Defines all of the routes for the App"""

from mealPlannerApp import mealPlanner
from flask import render_template, request
import os

mealPlanner.config["TEXT_IMPORT"] = "./static/uploads"

@mealPlanner.route('/display', methods=['POST'])
def todo():
    items = mealplanner.find()
    # items = [item for item in _items]
    lista = []
    print(items[0])
    for doc in items:
        lista.append(doc)

    if len(lista) == 0:#
        return render_template('vacio.html')#if no items, show vacio
    else:
        return render_template('todo.html', items=lista)


@mealPlanner.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form.get:

            date = request.form.get("date")
            meal1 = request.form.get("meal1")
            cook1 = request.form.get("cook1")
            dish1_1 = request.form.get("dish1_1")
            dish1_2 = request.form.get("dish1_2")
            meal2 = request.form.get("meal2")
            cook2 = request.form.get("cook2")
            dish2_1 = request.form.get("dish2_1")
            dish2_2 = request.form.get("dish2_2")

        day1 = create_day(str(date))

        dish1 = Dish(dish1_1)
        dish2 = Dish(dish1_2)
        dishes1 =[dish1,dish2]
        cook1 = Cook(cook1)
        cooks1 =[cook1]
        add_meal_to_day(day1, meal1, cooks1, dishes1)

        cooks2 = [Cook(cook2)]
        dishes2 = [Dish(dish2_1),Dish(dish2_1)]
        add_meal_to_day(day1, meal2, cooks2, dishes2)

        insert_entry_mongo(day1, mealplanner, "date")

    return render_template("testentry.html")


if __name__ == "__main__":
    mealPlanner.run(debug=True)
