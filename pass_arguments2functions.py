# Multiply two integers and display the result in a function

##def main():
##    val_1 = int(input('Enter an integer: '))
##    val_2 = int(input('Enter another integer: '))
##    multiply(val_1, val_2)
### Passing a value to an argument using parameter variables
##    value = 5
##    show_double(value)
##
##def multiply(val_1, val_2):
##    product = val_1 * val_2
##    print ('The result is', product)
##
### Passing a value to an argument 
##def show_double(number):
##	result = number * 2
##	print(result)
##
##main()


##  Write the definition of a function printGrade,
##  which takes one parameter containing a string value and returns nothing.
##  The function prints "Grade: " followed by the string parameter.

##def printGrade(grade):
##    print("Grade:", grade)

# Create a global variable
number = 0

# Define main function
def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is', number)

# Call the main function
main()


