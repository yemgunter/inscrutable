# Multiply two integers and display the result in a function

def main():
    val_1 = int(input('Enter an integer: '))
    val_2 = int(input('Enter another integer: '))
    multiply(val_1, val_2)
# Passing a value to an argument using parameter variables
    value = 5
    show_double(value)

def multiply(val_1, val_2):
    product = val_1 * val_2
    print ('The result is', product)

# Passing a value to an argument 
def show_double(number):
	result = number * 2
	print(result)

main()


