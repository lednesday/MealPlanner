from flask import Flask

mealPlanner = Flask(__name__)

from mealPlannerApp import routes
from entry import *
from helpers import *
