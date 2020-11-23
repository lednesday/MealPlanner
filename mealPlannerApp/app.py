"""Defines the flask Application instance"""

from flask import jsonify, Flask, render_template, request, redirect, url_for, abort, send_from_directory, g, flash
from entry import *
from helpers import *

import pymongo # modules
from pymongo import MongoClient

import datetime

'''
instance of Flask
'''
app = Flask(__name__)


'''
Connecting flask with MONGODB
'''
client = MongoClient("localhost", 27017) # connect to engine.
db = client["Project2"] # create database
mealplanner = db['Mealplanner']
# cook_database = db["cook"]
# recipe_database = db["Recipe"]
'''
Secret Key
Set's up secret key so flash messages can be displayed
'''
import configparser#import the key from secret file
config = configparser.ConfigParser()
config.read("credentials.ini")
# app.secret_key = config["DEFAULT"]["key_google"]
app.secret_key = "Holaaaaa"


'''
clean previous content of database(comment out when no needed for testing)
'''
"""Defines all of the routes for the App"""

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html", hide = 0)

@app.route("/cook", methods=["POST", "GET"])
def cook():

    mealplanners_names = return_dictionary_mongo_all(mealplanner)

    if request.method == "POST":
        cook_name = request.form.get("cook_name")
        cook_allergies = request.form.get("allergies")
        cook_restrictions = request.form.get("restrictions")
        cook_email = request.form.get("email")
        meal_plan  = request.form.get('meal_plan', None)
        print(return_dictionary_mongo_all(mealplanner))
        create_insert_cook(cook_name, cook_allergies, cook_restrictions, \
                           cook_email, meal_plan, mealplanner)

    return render_template("cook.html", mealplans_names=mealplanners_names, hide = 0)

@app.route("/recipe", methods=["POST", "GET"])
def recipe():

    mealplanners_names = return_dictionary_mongo_all(mealplanner)

    if request.method == "POST":
        mealPlanName = request.form.get("meal_plan")
        recipe_name = request.form.get("recipe_name")
        servings = request.form.get("yield")
        length = len(request.form.getlist("item"))
        item = request.form.getlist("item")
        quantity = (request.form.getlist("quantity"))
        unit = (request.form.getlist("unit"))
        ite = []
        ingredients = []
        for i in range(0, length):
            ite.append(item[i])
            ite.append(quantity[i])
            ite.append(unit[i])
            tuple_item = tuple(ite)
            ingredients.append(tuple_item)
            ite = []
        print(ingredients)

        directions = request.form.get("step")
        allergens = request.form.get("allergens")
        special_diets = request.form.get("restrictions")
        meal_plan  = request.form.get('meal_plan', None)

        create_insert_dish(recipe_name, servings, ingredients, directions, \
        					allergens, special_diets, meal_plan, mealplanner)

    return render_template("recipe.html", mealplans_names=mealplanners_names, hide=0)

@app.route("/newplan", methods=["POST", "GET"])
def newplan():
    if request.method == "POST":
        if request.form.get:
            plan_name = request.form.get("plan_name")
            start_date = request.form.get("start_date")
            end_date = request.form.get("end_date")
            checked_meals = request.form.getlist('meal0')
            checked = []
            if plan_name == "" and start_date == ""  and end_date == "":# case that the person hasn't input data.
                flash("No input provided.")
                return render_template("newplan.html")
            else:

                for i in range(0, len(date_range(start_date, end_date))):
                    temp = "meal"+str(i)
                    checked.append(request.form.getlist(temp))

                meal_plan = create_newplan(start_date, end_date , plan_name, checked)

                dates = date_range(start_date, end_date)# returns a list with all the dates bewtween start and end date.

                if insert_entry_mongo(meal_plan, mealplanner, "meal_plan") == True:
                    return render_template("newplan.html")
                else:
                    flash("New plan was added! ")
                return redirect(url_for("index"))

    return render_template("newplan.html", hide = 0)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    mealplanners_names = return_dictionary_mongo_all(mealplanner)
    meal_plan  = request.args.get('meal_plan', None)

    if request.method == "POST":
        meal_plan = request.form.get("meal_plan")
        list_cooks = drop_list_cooks(mealplanner, meal_plan)
        list_dishes = drop_list_recipes(mealplanner, meal_plan)
        one_mealplanner = return_dictionary_mongo(mealplanner, meal_plan)
        #drop_list_remove_already(mealplanner,meal_plan)
        return render_template("signup.html", list=one_mealplanner, mealplans_names=mealplanners_names, hide = 0, names = list_cooks, dishes = list_dishes)
    elif meal_plan != None:#for redirect from delete and add dish cook
        list_cooks = drop_list_cooks(mealplanner, meal_plan)
        list_dishes = drop_list_recipes(mealplanner, meal_plan)
        #drop_list_remove_already(mealplanner,meal_plan)
        one_mealplanner = return_dictionary_mongo(mealplanner, meal_plan)
        return render_template("signup.html", list=one_mealplanner, mealplans_names=mealplanners_names, hide = 0, names = list_cooks, dishes = list_dishes)

    return render_template("signup.html", mealplans_names=mealplanners_names, hide = 0)


'''
experiment. Send link by email for users to add cooks and dishes. Users should be available
to edit but not able to see other links
'''
@app.route('/plan/<plan_name>')
def landing_page(plan_name):
    print("plan")
    list_mealplans = return_dictionary_mongo(mealplanner, plan_name)
    return render_template("signup.html", list=list_mealplans, hide=1)


'''
checks if name is in database.
TODO check for no spaces.
'''
@app.route("/_check_name")#function to check names. Connects to js in newsplan/
def check_name():
    name = request.args.get("text", type=str)
    list_mealplan = retrieve_data_index_list(mealplanner)# checks names in the mealplan to check if exists.

    if name == "":
        rslt = {"response": "Zero"}
    elif name in list_mealplan:
        rslt = {"response": "Yes"}
    else:
        rslt = {"response": "No"}

    return jsonify(result=rslt)


'''
return an array with dates to generate fields in signup
'''
@app.route("/_count_inputs", methods=["POST", "GET"])
def count_inputs():
    start_date = request.args.get("start", type=str)
    end_date = request.args.get("end", type=str)
    dates_range = date_range(start_date, end_date)
    full_date = []
    for i in dates_range:
        full_date.append(datetime.datetime.strptime(i, '%Y-%m-%d').strftime('%A, %d %B of %Y'))

    rslt = {"dates_range": full_date}

    return jsonify(result=rslt)


@app.route("/add_cook", methods=["POST", "GET"])
def add_cook():

    date  = request.args.get('date', None)
    meal  = request.args.get('meal', None)
    planner_name  = request.args.get('planner_name', None)
    cook = request.form.get("cook")
    print(cook)
    if cook != "":
        cooks_in_database = get_cooks_mongo(mealplanner, planner_name, date, meal)
        if cook not in cooks_in_database:
            add_cook_mongo(mealplanner, planner_name, date, meal, cook)
        else:
            flash('"' +cook +'" is already registered. ')

    one_mealplanner = return_dictionary_mongo(mealplanner, planner_name)
    return redirect(url_for('signup', meal_plan = planner_name))


@app.route("/add_dish", methods=["POST", "GET"])
def add_dish():
    planner_name  = request.args.get('planner_name', None)
    list_mealplans = return_dictionary_mongo(mealplanner, planner_name)
    date  = request.args.get('date', None)
    meal  = request.args.get('meal', None)
    dish = request.form.get("dish")
    if dish != "":
        dishes_in_database = get_dishes_mongo(mealplanner, planner_name, date, meal)
        if dish not in dishes_in_database:
            add_dish_mongo(mealplanner, planner_name, date, meal, dish)
        else:
            flash('"' +dish +'" is already registered. ')

    one_mealplanner = return_dictionary_mongo(mealplanner, planner_name)
    return redirect(url_for('signup', meal_plan = planner_name))

@app.route("/delete_dish", methods=["POST", "GET"])
def delete_dish():
    # args from website
    dish_delete  = request.args.get('dish_delete', None)
    planner_name  = request.args.get('planner_name', None)
    date  = request.args.get('date', None)
    meal  = request.args.get('meal', None)
    delete_dish_mongo(mealplanner, planner_name, date, meal, dish_delete)
    return redirect(url_for('signup', meal_plan = planner_name))

@app.route("/delete_cook", methods=["POST", "GET"])
def delete_cook():
    # args from website
    cook_delete  = request.args.get('cook_delete', None)
    planner_name  = request.args.get('planner_name', None)
    date  = request.args.get('date', None)
    meal  = request.args.get('meal', None)
    delete_cook_mongo(mealplanner, planner_name, date, meal, cook_delete)
    return redirect(url_for('signup', meal_plan = planner_name))

if __name__ == "__main__":
    app.run(debug=True)
