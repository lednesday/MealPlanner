# one day can have several meals and cooks
# meals can have one of several cooks
# meals can have several recipes (i.e. "breakfast" contains coffe, club sandwich and boiled eggs)
# a recipe can have several ingredients (i.e. "club sandwich" has ham, bacon, bread. One class for ingredientes and another for preparation)

#RESEARCH INHERINTANCE.
class Day:  #The program would create an array of days, each one containing
    def __init__(self, date:str):  # creates day but it can add meals and cooks later. Date is required
        self.__meal = []# list of meals objects
        self.__date = date  # date (it cannot be changed, for now)

    def get_date(self):
        return self.__date# return date when the cook shift is happening

    def add_meal(self, meal): # meal is a Meal() object
        self.__meal.append(meal)

    def get_meal(self):  # return the meals (an array)
        for i in self.__meal:
            print(i.get_meal())
        return self.__meal

class Meal:

    def __init__(self, meal: str):  # "meal" is string, breakfast, lunch or dinner
    #recipe is an object but meanwhile, I put it as string.
        self.__meal = meal # string
        self.__recipe = [] # for the moment, string
        self.__cook = []# temporal, cook and meal would be an list of object (using strings meanwhile)

    def add_recipe(self, recipe: str): # "recipe" (or dish) is an object (recipe object contain name, ingredients, allergies and instructions), meanwhile, string.
        self.__recipe.append(recipe) # "recipe" should have an attribute for allergies

    def add_cook(self, new_cook:str):
        self.__append(new_cook)# add cook per meal. There is different meals through the day but it can be different cooks

    def get_recipe(self):
        return self.__recipe

    def get_meal(self):
        return self.__meal

    def get_cook(self):
        return self.__cook
