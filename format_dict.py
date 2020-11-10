import pymongo # modules
from pymongo import MongoClient


dict = {'date': '11-4-20', 'meals': {'Breakfast': {'dishes': ['Eggs', 'Bacon', 'French Toast'], 'cooks': ['Antonio', 'Milagros', 'Jose']}, 'Lunch': {'dishes': ['Chilaquiles', 'Bacon', 'Toast'], 'cooks': ['Jack', 'Anna', 'Jose']}}}


list = []

for item in dict['meals'].items():
    list.append(item)

print(list[0][0])
print(list[0][1]['dishes'])
print(list[0][1]['cooks'])
