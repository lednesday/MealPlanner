from flask import Flask

mealPlanner = Flask(__name__)

@mealPlanner.route("/")
def index():
    return "Meal Planner";

if __name__ == "__main__":
    mealPlanner.run(debug=True, host="0.0.0.0", port=3000)