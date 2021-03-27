# Multiply two integers and display the result in a function

def main():
    val_1 = int(input('Enter an integer: '))
    val_2 = int(input('Enter another integer: '))
    multiply(val_1, val_2)

def multiply(num_1, Num_2):
    product = num_1 * num_2
    print ('The result is', product)

main()
