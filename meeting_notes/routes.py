from entry import *
from helpers import *

import pymongo # modules
from pymongo import MongoClient
from mealPlannerApp import mealPlanner
from flask import render_template, request, url_for, redirect

client = MongoClient("localhost", 27017) # connect to engine.
'''
clean previous content of database
'''
db = client["Project2"] # create database
mealplanner = db['Mealplanner']
# mealplanner.drop()
cook_database = db["cook"]
recipe_database = db["Recipe"]

"""Defines all of the routes for the App"""

from mealPlannerApp import mealPlanner
from flask import render_template, request, url_for, redirect


mealPlanner.config["TEXT_IMPORT"] = "./static/uploads"


@mealPlanner.route('/display', methods=['POST'])
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


@mealPlanner.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@mealPlanner.route("/newplan", methods=["POST", "GET"])
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


@mealPlanner.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        return redirect(url_for("index"))

    return render_template("signup.html")

if __name__ == "__main__":
    mealPlanner.run(debug=True)
