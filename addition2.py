

def main(): # This is calling the function
    # Read two integers
    x = int(input("Enter and interget: "))
    y = int(input("Enter and interget: "))

    add_numbers(x, y)

    
#######################################################
# Function name: add numbers
# Purpose:       This function displays the sum
#                of two integers and displays the sum
#                
# Input:         Two intergers
# Output:        None
#######################################################

def add_numbers(num1, num2): # first define function
   

    # Calculate abd display the sumn
    total = num1 + num2
    print("The sum is", total)



main()
