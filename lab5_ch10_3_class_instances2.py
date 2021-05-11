##Write the class Calculator including:
##    
##a function called addthat takes two parameters containing double
##values and returns their sum
##
##a function called subtractthat takes two parameters
##containing double values and returns their difference
##(subtract the second from the first)
##
##a function called multiply that takes two parameters containing
##double values and returns their product
##
##a function called divide that takes two parameters containing
##double values and returns the value of the first divided by the
##second. If the second number is a zero, do not divide,
##and return "You can't divide by zero!"



class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1*num2
    
    def divide(self, num1, num2):
        if num2==0:
            return "You can't divide by zero!"
        else:
            return num1/num2
