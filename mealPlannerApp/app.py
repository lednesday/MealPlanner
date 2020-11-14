"""Defines the flask Application instance"""

from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory, g, flash
from entry import *
from helpers import *

import pymongo # modules
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("localhost", 27017) # connect to engine.
db = client["Project2"] # create database

mealplanner = db['Mealplanner']

'''
clean previous content of database(comment out when no needed for testing)
'''
# mealplanner.drop()

cook_database = db["cook"]
recipe_database = db["Recipe"]

"""Defines all of the routes for the App"""

# from mealPlannerApp import mealPlanner
# from flask import render_template, request
# import os
# mealPlanner.config["TEXT_IMPORT"] = "./static/uploads

# @app.route('/display', methods=['POST'])
# def todo():
#     # items = mealplanner.find()
#     # array = list(mealplanner.find())
#     list_result = []
#     for day in mealplanner.find({},{"_id": 0, "date": 1, "meals": 1} ):
#         list_result.append("Date: " + str(day['date']) + " Meals:" + str(day['meals']))
#
#     if len(list_result) == 0:#
#         return render_template('vacio.html')#if no items, show vacio
#     else:
#         return render_template('todo.html', items=list_result)


# @app.route("/", methods=["POST", "GET"])
# def index():
#
#     list_cooks = retrieve_data_index_list(cook_database, "name")
#     list_dishes = retrieve_data_index_list(recipe_database, "title")
#
#     if request.method == "POST":
#         if request.form.get:
#             date = request.form.get("date")
#             meal1 = request.form.get("meal1")
#             cook1 = request.form.get("cook1")
#             dish1_1 = request.form.get("dish1-1")
#             dish1_2 = request.form.get("dish1-2")
#             meal2 = request.form.get("meal2")
#             cook2 = request.form.get("cook2")
#             dish2_1 = request.form.get("dish2-1")
#             dish2_2 = request.form.get("dish2-2")
#
#             day1 = create_day(date)
#             dishes1 = []
#             cooks1 = []
#             if meal1 != "":
#                 if dish1_1 != "":
#                     dish1_o = Dish(dish1_1)
#                     dishes1.append(dish1_o)
#                 if dish1_2 != "":
#                     dish2_o = Dish(dish1_2)
#                     dishes1.append(dish2_o)
#                 if cook1 != "":
#                     cook1_o = Cook(cook1)
#                     cooks1.append(cook1_o)
#                 add_meal_to_day(day1, meal1, cooks1, dishes1)
#
#             dishes2 = []
#             cooks2 = []
#             if meal2 != "":
#                 if dish2_1 != "":
#                     dish1_o = Dish(dish2_1)
#                     dishes2.append(dish1_o)
#                 if dish2_2 != "":
#                     dish2_o = Dish(dish2_2)
#                     dishes2.append(dish2_o)
#                 if cook2 != "":
#                     cook2_o = Cook(cook2)
#                     cooks2.append(cook2_o)
#                 add_meal_to_day(day1, meal2, cooks2, dishes2)
#
#             if day1.number_meals() != 0:
#                 insert_entry_mongo(day1, mealplanner, "date")
#
#     return render_template("testentry.html", names = list_cooks, dishes = list_dishes)



@app.route('/display', methods=['POST'])
def todo():
    # items = mealplanner.find()
    # array = list(mealplanner.find())
    list_result = []
    for day in mealplanner.find({},{"_id": 0, "date": 1, "meals": 1} ):
        list_result.append("Date: " + str(day['date']) + " Meals:" + str(day['meals']))

    print(list_result)

    if len(list_result) == 0:
        return render_template('vacio.html')  #  if no items, show vacio
    else:
        return render_template('todo.html', items=list_result)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/newplan", methods=["POST", "GET"])
def newplan():
    if request.method == "POST":
        if request.form.get:
            date = request.form.get("plan_name")
            print(date)
            start_date = request.form.get("start_date")
            print(start_date)
            end_date = request.form.get("end_date")
            print(end_date)
            checked_meals = request.form.getlist('meal')
            print(checked_meals)


        return redirect(url_for("index"))

    return render_template("newplan.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        return redirect(url_for("index"))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
