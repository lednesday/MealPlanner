from entry import *

'''
We create one day at the time
Input: date we want to add
output: Day object
'''
def create_day(date_event: str):
    return Day(date_event)

'''
It adds one meal at the time (breakfast, lunch or dinner)
one day can have many meals, one meal can have many dishes and many cooks
(we assume that all the cooks of one meal helps out with all the dishes of that meal)
input: day object, meal name, cooks list and dishes list.
output: None but it modify the Day Object
'''
def add_meal_to_day(day: Day, meal:str, cooks: list, dishes: list): #cooks and dishes are list.
    temp = Meal(meal)
    for i in cooks:
        temp.add_cook(i)
    for j in dishes:
        temp.add_dish(j)
    day.add_meal(temp)

'''
extract the info inside the day object and convert it to dictionary, which is compatible to be storage into mongo. at last, it will insert it into the dictionary.
'''
def insert_entry_mongo(day: Day, collection):
    temp = collection.insert_one(day.get_json())
    del day #delete day object since it is already in the database NEED TO BE CHECK
    return temp #id returned

'''
deletes entry according to the date
input: mongo collection
output: delete by date
'''
def delete_entry_mongo(collection, date_delete: str):
    myquery = { "date": date_delete }
    collection.delete_one(myquery)

'''
Modify cooks
TODO
"check if info is inside before trying to modify, otherwise, it will just add the info"
'''
def modify_cooks(collection, date: str, meal:str, cooks: list):
    collection.update_one({"date":date},{"$set":{"Meals."+ meal +".cooks":cooks}})

'''
Modify meals
'''
def modify_dishes(collection, date: str, meal:str, dishes: list):
    # collection.update_one({"date":date},{"$unset":{"dishes":dishes}})
    collection.update_one({"date":date},{"$set":{"Meals."+ meal +".dishes":dishes}})

'''
retrive specific data
for now, I am using date as an index to find entries

TODO:
practice to get more specific data from the database
'''
def retrieve_data(collection, date: str, field: str):
    result = collection.find({"date":date}) #
    # for doc in result:
    return result[0][field]['Breakfast']['cooks']
