
'''
This is a file to test the creation and deletion of objects and database info
related to the mealPlannerApp program.

If there was not enough time to make these, then you will see only two commented
out functions for the database: drop and print.

MAKE SURE YOU HAVE THE FILES IN requirements.txt INSTALLED ON YOUR COMPUTER OR
ENVIRONMENT. TO INSTALL THEM, SEE docs/build.txt
'''

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

'''
To drop databases
'''
# mealplanner.drop()
# client.drop_database("Project2")

'''
Only works when a mealPlanner has days in it
'''
#print_database(mealplanner)