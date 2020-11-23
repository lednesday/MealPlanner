#23:35
from entry import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient
from cook_variables import * #for testing variables


client = MongoClient('mongodb+srv://new-user-31:new-user-31@cluster0.yev3v.mongodb.net/flask-mongodb-atlas?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE') # connect to engine.
'''
clean previous content of database
'''
# client.drop_database("cook")
db = client.Project2  # create database
cook_database = db.cook
# cook_database.drop()

class Cook:
    '''
    A cook is a person who will cook the meal. Each meal has one or more
    assigned cooks.
    '''

    def __init__(self, name:str):
        '''
        creates day but it can add meals and cooks later. Date is required
        '''
        self.__name = name # Cook's name
        self.__extra = [] # Cook's name

    def get_index(self):
        return self.__name

    def add_extra(self, info: str):
        '''
        add random info from cook (i.e. allergies, if prefer not to cook meat, etc)
        For now, it will add the info as a lidst of strings, one by one
        '''
        temp = info.split(", ")
        for i in temp:
            self.__extra.append(i) #

    def get_dictionary(self):
        temp = {"name": self.__name , "extra": self.__extra}
        return temp

def create_insert_cook(name: str, extra:str, collection):
    temp = Cook(name)
    temp.add_extra(extra)
    insert_entry_mongo(temp, collection, "name")

create_insert_cook("Antonio", cook1, cook_database)
create_insert_cook("Jose", cook2, cook_database)
create_insert_cook("Melissa", cook3, cook_database)
create_insert_cook("Johny", cook4, cook_database)
create_insert_cook("Vanessa", cook5, cook_database)
create_insert_cook("Maria", cook6, cook_database)
create_insert_cook("Ursula", cook7, cook_database)
create_insert_cook("Gabriel", cook8,cook_database)
create_insert_cook("Manuel", cook9, cook_database)
create_insert_cook("Ines", cook10, cook_database)
print_database(cook_database)

'''
Get names of cooks as lists
'''

for i in retrieve_data_index_list(cook_database, "name"):
    print(i)
