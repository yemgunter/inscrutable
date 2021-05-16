###############################################################
# Yolanda Gunter
#  Lab 5            
# My program uses the input file and work with the data as objects to
# run program that asks User for current date, reads a contact file
# that contains names with DOB, calculate each contact's age,
# season born in and born in a leap year or not.
# Then my program will print the calculated average age of contacts.
##############################################################

########################################################
# Function name: main
# Input: contactsLab5.txt file
# Output: table of contact, age, birth season & if born leap yr or not 
# Purpose: This function reads file, process it as a strings, converts
# strings to integers, calculates ages, season born & if born leap yr
# or not then lastly calculats average age of contacts in entire file.
###############################################

import lab5_class_Gunter

def main():
    try:
        friends_file = open("contactsLab5.txt", 'r')
        friend_list = []

        name = friends_file.readline()
        while name != "":
            name = name.rstrip('\n')       
            birthdate = friends_file.readline().rstrip('\n')     
            a_friend = lab5_class_Gunter.Contact(name, birthdate)
            friend_list.append(a_friend)
            
            name = friends_file.readline()
        
        friends_file.close()
     
        display_friends(friend_list)
    except FileNotFoundError:
        print("File was not found")
    except Exception as err:
        print("Error:", err)

#################################################
### Function name: display_contacts
### Input: names and birthdates isolated as variables
### Output: names, ages birth season, birth year is leap or not 
### Purpose: Display table of data calculated from functions    
##############################################       
    
def display_friends(chums):
    # Get current date
    todays = input("Enter current date in the format 'month d, yyyy': ")

    # initiates total age to use in average age calculation
    total_age = 0

    
    print(format("Name", '20'), format("Age", '7'),
          format("Season", '10'), format("Leap Year?", '5'))
    print(format("----------", '20'), format("-----", '7'),
          format("------", '10'), format("---------", '5'))
    for i in range(len(chums)):

        ages = int(chums[i].calculate_age(todays))

        total_age += ages
        
        print(format(chums[i].get_name(), '20'), \
              format(str(chums[i].calculate_age(todays)), '7'), \
              format(chums[i].find_season(), '10'), \
              format(chums[i].is_leap_year(), '5'))
    
    print("\nAverage age of contact is ", total_age // len(chums))

    
main()



