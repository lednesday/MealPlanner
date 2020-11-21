
from entry import *
from helpers import *
import pymongo # modules
from pymongo import MongoClient
from cook_variables import * #for testing variables


client = MongoClient("localhost", 27017) # connect to engine.
'''
clean previous content of database
'''
#client.drop_database("cook")
db = client["Project2"] # create database
cook_database = db["cook"]
cook_database.drop()

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
        self.__allergies = [] # Cook's allergier
        self.__restrictions = [] # Vegan, Gluten-free, etc
        self.__email = ""

    def get_index(self):
        return self.__name

    def add_email(self, email:str):
        self.__email = email


    def add_allergies(self, allergies: str):
        '''
        add random info from cook (i.e. allergies, if prefer not to cook meat, etc)
        For now, it will add the info as a lidst of strings, one by one
        '''
        temp = allergies.split(", ")
        for i in temp:
            self.__allergies.append(i)

    def add_restrictions(self, info: str):
        '''
        add random info from cook (i.e. allergies, if prefer not to cook meat, etc)
        For now, it will add the info as a lidst of strings, one by one
        '''
        temp = info.split(", ")
        for i in temp:
            self.__restrictions.append(i)

    def get_dictionary(self):
        temp = {"name": self.__name , "allergies": self.__allergies, \
                "restrictions": self.__restrictions, "email" : self.__email}
        return temp

def create_insert_cook(name: str, allergies:str, restrictions:str, email:str, collection):
    temp = Cook(name)
    temp.add_allergies(allergies)
    temp.add_restrictions(restrictions)
    temp.add_email(email)
    insert_entry_mongo(temp, collection, "name")

create_insert_cook("Dummy", "Peanuts, fish", "Vegan", "dummytest@gmailcom", cook_database)

'''
create_insert_cook("Antonio", cook1[0], cook1[1], cook_database)
create_insert_cook("Jose", cook2[0], cook2[1], cook_database)
create_insert_cook("Melissa", cook3[0], cook3[1], cook_database)
create_insert_cook("Johny", cook4[0], cook4[1], cook_database)
create_insert_cook("Vanessa", cook5[0], cook5[1], cook_database)
create_insert_cook("Maria", cook6[0], cook6[1], cook_database)
create_insert_cook("Ursula", cook7[0], cook7[1], cook_database)
create_insert_cook("Gabriel", cook8[0], cook8[1],cook_database)
create_insert_cook("Manuel", cook9[0], cook9[1], cook_database)
create_insert_cook("Ines", cook10[0], cook10[1], cook_database)
'''

print_database(cook_database)


'''
Get names of cooks as lists
'''

for i in retrieve_data_index_list(cook_database, "name"):
    print(i)
