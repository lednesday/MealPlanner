"""Defines all of the routes for the App"""

from mealPlannerApp import mealPlanner
from flask import render_template, request
import os

mealPlanner.config["TEXT_IMPORT"] = "./static/uploads"


@mealPlanner.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form.get:
            #  Saving plan name in text file
           # planName = request.form.get("plan_name")
           # with open(os.path.join(mealPlanner.config["TEXT_IMPORT"], "plan_name.txt"), "w") as filename:
           #     filename.write(planName)
           # print("Plan Name Saved")

            #  Saving start date in text file
           # start_date = request.form.get("start_date")
           # with open(os.path.join(mealPlanner.config["TEXT_IMPORT"], "start_date.txt"), "w") as filename:
            #    filename.write(start_date)
            #print(start_date)
            #print("Start Date Saved")

            #  Saving end date in text file
            #end_date = request.form.get("end_date")
            #with open(os.path.join(mealPlanner.config["TEXT_IMPORT"], "end_date.txt"), "w") as filename:
            #    filename.write(end_date)
            #print("End Date Saved")

            #  Check which boxes are checked
           # breakfast = False
           # if request.form.getlist("meal"):
           #     breakfast = True
           #     print("Breakfast was checked")
           # lunch = False
           # if request.form.get("meal"):
           #     lunch = True
           #     print("Lunch was checked")
           # dinner = False
           # if request.form.get("meal"):
           #     dinner = True
           #     print("Dinner was checked")
           # snacks = False
           # if request.form.get("meal"):
            #    snacks = True
             #   print("Snacks were checked")
            date = request.form.get("date")
            print(date)
            meal1 = request.form.get("meal1")
            print(meal1)
            cook1 = request.form.get("cook1")
            print(cook1)
            dish1_1 = request.form.get("dish1_1")
            print(dish1_1)
            dish1_2 = request.form.get("dish1_2")
            print(dish1_2)
            meal2 = request.form.get("meal2")
            print(meal2)
            cook2 = request.form.get("cook2")
            print(cook2)
            dish2_1 = request.form.get("dish2_1")
            print(dish2_1)
            dish2_2 = request.form.get("dish2_2")
            print(dish2_2)

    return render_template("testentry.html")


if __name__ == "__main__":
    mealPlanner.run()