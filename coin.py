# coin class simulates a coin that can be flipped

import random

class Coin:

    # __init__ method initializes the sideup data
    # attribute with tails
    def __init__(self):
        self.__sideup = "heads"

    # the get_sideup method returns the value
    # referenced by sideup
    def get_sideup(self):
        return self.__sideup

    # the toss method generates a random number
    # in range 0 thru 1. if 0, sideup set to 'heads'
    # Otherwise, sideup is set to 'tails'
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "heads"
        else:
            self.sideup = "tails"
