# Pulling libraries
import random
import math

def main():
    times = int(input("How many times? "))
    lower = int(input("Enter lower range: "))
    upper = int(input("Enter upper range: "))

    
    for i in range(times):
        rand_num = get_random_num(lower, upper)
        print("The squre root of", rand_num, "is",
              format(get_sqrt(rand_num), '.4f'))

    print(format(1.25, '.1f
    
##    #Minimum code to test program
##    for i in range(10):
##        print(get_random_num(1, 10))  


def get_random_num(lower, upper):
    random_num = random.randint(lower, upper)
    return random_num


def get_sqrt(num):
    
    return math.sqrt(num)
    


main()
