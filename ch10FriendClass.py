
class Friend:

    def __init__(self, name, age, food):
        self.__name = name
        self.__age = age
        self.__food = food

    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_food(self, food):
        self.__food = food

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_food(self):
        return self.__food

    def __str__(self):
        return "Name: " + self.__name + '\n' + \
               "Age: " + str(self.__age) + '\n' + \
               "Favortie food: " + self.__food
