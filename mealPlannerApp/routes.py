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
            planName = request.form.get("plan_name")
            with open(os.path.join(mealPlanner.config["TEXT_IMPORT"], "plan_name.txt"), "w") as filename:
                filename.write(planName)
            print("Plan Name Saved")

            #  Saving start date in text file
            start_date = request.form.get("start_date")
            with open(os.path.join(mealPlanner.config["TEXT_IMPORT"], "start_date.txt"), "w") as filename:
                filename.write(start_date)
            print("Start Date Saved")

            #  Saving end date in text file
            end_date = request.form.get("end_date")
            with open(os.path.join(mealPlanner.config["TEXT_IMPORT"], "end_date.txt"), "w") as filename:
                filename.write(end_date)
            print("End Date Saved")

            #  Check which boxes are checked
            breakfast = False
            if request.form.getlist("meal"):
                breakfast = True
                print("Breakfast was checked")
            lunch = False
            if request.form.get("meal"):
                lunch = True
                print("Lunch was checked")
            dinner = False
            if request.form.get("meal"):
                dinner = True
                print("Dinner was checked")
            snacks = False
            if request.form.get("meal"):
                snacks = True
                print("Snacks were checked")

    return render_template("newplan.html")


if __name__ == "__main__":
    mealPlanner.run()