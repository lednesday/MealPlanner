"""Defines all of the routes for the App"""

from mealPlannerApp import mealPlanner
from flask import render_template


@mealPlanner.route("/")
def index():
    return render_template("base.html")


if __name__ == "__main__":
    mealPlanner.run()