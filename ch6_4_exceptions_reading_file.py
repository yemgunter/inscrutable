# chapter 6 reboot 5/2/21 Saturday to beat Lab 4 to death
# replay lectures from 3/30 Tuesday

def main:


################ 6.4 3/30/21 lecture Exceptions  ##########
# this program will read the records out of the file then display them

    try:
        #open the file
        friends = open('friends2.txt', 'r') 

        # read first line name field
        name = friends.readline()

        #if a field is read establish records
        while name != "":
            
            #strip \n from name field
            name = name.rstrip('\n')

            #convert strin age to interger
            age = int(friends.readline())
            
            #strip \n from food field
            food = friends.readline().rstrip('\n') 

            
            print(name, age, food)
            name = friends.readline()

        friends.close()

    #file not found exception
    except FileNotFoundError: 
        print("File was not found") 
    except Exception as err:
        print("Error:", err)
    

main()


################ 6.4 3/30/21 lecture Exceptions  ##########
##    try: #signals start of exception
##        num = int(input("Enter an integer: "))
##
##        print("You entered", num)
##
##        result = num / 0
##
##    except ValueError: #exception at input
##        print("Invalid value - must be number")
##    except TypeError: #exception with int function
##        print("Error calling the input frunction")
##    except as error: #name the error
##        print("An unknown error has occurred")
