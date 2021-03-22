## Defining and Calling a FUNCTION Ch 5.2 Void Function


### FIRST, define a function named message.
##def message():
##    print('I am Arthur')
##    print('King of Zoos')
##    
### CALL the message function
##message()

# FIRST, define a function named main to memory,
# SECOND, define function named message to memory,
# THIRD, sees call to main,
# FOURTH, executes main from memory,
# FIFTH, sees call message within main,
# SIXTH, execute message from memory,
# LASTLY, continues within main to print & ends program.

def main():
    print('I have a message for you.')
    message()
    print('Later!')
    
def message():
    print('I am Arthur')
    print('King of Zoos')

main()



# this program does not take any input

##def main():
##    
##    print("This program will call a function")
##
##    user_message = input("Enter a message: ")
##    
##    message(user_message)
##
##    print("The function has been called")
##
##def message(msg):
##    print(msg)
##
##
##main()

