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

"""Defines all of the routes for the App"""

from mealPlannerApp import mealPlanner
from flask import render_template, request
import os

mealPlanner.config["TEXT_IMPORT"] = "./static/uploads"


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
        cooks1 =[]
        cooks1.append(str(cook1))
        dishes1 =[]
        dishes1.append(str(dish1_1))
        dishes1.append(str(dish1_2))
        add_meal_to_day(day1, meal1, cooks1, dishes1)
        cooks2 = []
        cooks2.append(str(cook2))
        dishes2 = []
        dishes2.append(str(dish2_1))
        dishes2.append(str(dish2_2))

        print(cooks1)
        print(cooks2)
        print(dishes1)
        print(dishes2)

        add_meal_to_day(day1, meal2, cooks2, dishes2)
        day1.get_dictionary()
        # insert_entry_mongo(day1, mealplanner, "date")
        # print_database(mealplanner) # print content so far

    return render_template("testentry.html")


if __name__ == "__main__":
    mealPlanner.run(debug=True)
