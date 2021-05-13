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
# Input: contactsLab4.txt file
# Output: table of contact, age, birth season & if born leap yr or not 
# Purpose: This function reads file, process it as a strings, converts
# strings to integers, calculates ages, season born & if born leap yr
# or not then lastly calculats average age of contacts in entire file.
###############################################

import lab5_class_Gunter

def main():
    try:
        # Open a file named contactlab4.txt
        contacts_file = open('contactsLab5.txt', 'r')
        contacts_list = []

        # Read first name from the file
        name = contacts_file.readline()
        while name != '':
            # remove \n from name
            name = name.rstrip('\n')
            # read birthdate, remove \n frm birthdate
            birthdate = contacts_file.readline().rstrip('\n')
            a_contact = lab5_class_Gunter.Contact(name, birthdate)
            for i in a_contact:
                contacts_list.append(a_contact(i))

            # read next name from file
            name = contacts_file.readline()
            
        contacts_file.close()
       
        display_friends(a_contact)
    
        

    # Simple exception if file is not found
    except FileNotFoundError:
        print("File was not found")
        
    except Exception as err:
        print("Error:", err)


def display_friends(chums):           
    print(format("Name", '20'), format("Birthdate", '25'))
    for i in range(len(chums)): 
        print(format(chums[i].get_name(), '20'),
              format(chums[i].get_birthdate(), '25'))


            
#################################################
### Function name: display_contacts
### Input: names and birthdates isolated as variables
### Output: names, ages birth season, birth year is leap or not 
### Purpose: Display table of data calculated from functions    
###############################################
##def display_contacts(chums):    
##    # Get current date
##    current_date = input('Enter current date in format month d, yyyy: ')
##
##    # initiates total age to use in average age calculation
##    total_age = 0
##    
##    # format display in table format with column headings
##    print(format("Name", '25'), format("Age", '5'), \
##          format("Season", '8'), format("Leap Year", '10'))
##    print(format("-------", '25'), format("-----", '5'), \
##          format("-----", '8'), format("---------", '10'))
##    for i in range(len(chums)):
##        # get contact's age
##        age = get_age(current_date, birthdates[i])
##        # accumulate ages for the average age calculation
##        total_age += age
##        
##        print(format(names[i], '25'), \
##              format(str(age), '5'), \
##              format(find_season(birthdates[i]), '8'), \
##              format(is_leap_year(birthdates[i]), '10'));
##
##    # calculate and display the average age of contacts
##    print("\nAverage age of contact is ", total_age // len(chums))
##
##
    

# Call the main function
main()


