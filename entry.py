'''
order: The system creates one day at the time. We fill it up with the date, the meals, the cooks and dishes.
'''

class Day:
    '''
    The program would create an array of days, each one containing
    '''
    def __init__(self, date:str):
        '''
        creates day but it can add meals and cooks later. Date is required
        '''
        self.__date = date  # date (it cannot be changed, for now)
        self.__meal = []# list of meals objects

    def get_date(self):
        return self.__date# return date when the cook shift is happening

    def add_meal(self, meal): # meal is a Meal() object
        self.__meal.append(meal)

    def get_meal(self):  # return the meals (an array)
        for i in self.__meal:
            print(i.get_meal())
        return self.__meal

    def get_json(self):
        '''
        It will format all the info of the object into a json format ready to be inserted in mongodb
        '''

        result = '{"date": "' + str(self.get_date())+'","Meals": {'

        for i in self.__meal:
            dishes = ""
            cooks = ""

            result += '"' + i.get_meal() + '":{"dishes": '+ str(i.get_dishes()) +', "cooks":'+ str(i.get_cooks()) +'},'

        result = result[:-1]
        result += "}}"

        diccionary = eval(result)
        return diccionary

class Meal:
    '''
    "meal" is string, (breakfast, lunch, dinner, etc)
    dish is an object (may contain recipe) but meanwhile, I put it as string.
    '''
    def __init__(self, meal: str):
        self.__meal = meal # string (breakfast, lunch, dinner)
        self.__dish = [] # for the moment, string
        self.__cook = []# temporal, cook and meal would be an list of object (using strings meanwhile)
    '''
    dishes an object (recipe object contain name, ingredients, allergies and instructions), meanwhile, string.
    '''
    def add_dish(self, dish: str):
        self.__dish.append(dish) # "recipe" should have an attribute for allergies

    '''
    self.__cooks is a list of string with names. It may be good to convert it into an object
    '''
    def add_cook(self, new_cook:str):
        self.__cook.append(new_cook)# add cook per meal. There is different meals through the day but it can be different cooks

    def get_dishes(self):
        return self.__dish

    def get_meal(self):
        return self.__meal

    def get_cooks(self):
        return self.__cook
