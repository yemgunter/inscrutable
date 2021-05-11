##############################################################
# Lab 4 Solution                                             #
# This program reads contact information from a file.        #
# Each record contains two fields:                           #
#      1. Contact name                                       #
#      2. Contact birthdate in the form m/d/yyyy             #
# It will display for each contact:                          #
#   Name, age, season born and whether it was a leap year    #
# After displaying all of the info about the contacts, it    #
# will display the average age of the contacts.              #
##############################################################

def main():
    # Set up lists to be used for names and birthdates
    names = []
    birthdates = []
    
    try:
        # Open the contacts file for input
        infile = open("contactsLab4.txt", 'r')

        # Read the first name from the file
        name = infile.readline()
        while name != '':
            # Remove the newlie from name
            name = name.rstrip('\n')
            # Read birthdate
            birthdate = infile.readline().rstrip('\n')

            # Put the name in the names list
            names.append(name)

            # Put the birthdate in the birthdates list
            birthdates.append(birthdate)

            # Read the next name from the file
            name = infile.readline()
           
        # Close file
        infile.close()

        display_contacts(names, birthdates)

    # Check for invalid file name
    except FileNotFoundError:
        print("Error: Invalid file name")

    except Exception as error_msg:
        print("Error:", error_msg)        
        
#####################################################
# Function name: display_contacts                   #
# Input: The lists of names and birthdates          #
# Output: none                                      #
# Purpose: This function displays in a table, the   #
#          names, ages, seasons born and whether    #
#          their birth year was a leap year or not  #
#####################################################
def display_contacts(contact_names, contact_birthdates):
    # Get the current date from the user
    current_date = input("Enter the current date in the format m/d/yyyy: ")

    # Initialize the total age and number of contacts
    # to use in the average age calculation
    total_age = 0

    # Display column headings
    print(format("Name", '25'), format("Age", '5'), format("Season born", '15'),
          format("Leap year?", '10'))
    print(format("-----", '25'), format("----", '5'), format("------------", '15'),
          format("----------", '10'))
    for i in range(len(contact_names)):
        # Get contact's age
        age = get_age(current_date, contact_birthdates[i])
        # Accumulate ages for the average age calculation
        total_age += age
        
        # Get the season
        season = find_season(contact_birthdates[i])

        # Call function to determine if the year was a leap year or not
        if is_leap_year(contact_birthdates[i]):
            leap_year = 'Yes'
        else:
            leap_year = 'No'

        # Display info for one contact
        print(format(contact_names[i],'25'),format(str(age), '5'),
              format(season,'15'), format(leap_year, '10'));

    # Calculate and display the average age of the contacts
    print("\nAverage age of contact is ", total_age // len(contact_names))

#####################################################
# Function name: get_age                            #
# Input: current date string in the format m/d/yyyy #
#        birthdate string in the format m/d/yyyy    #
# Output: current age as an integer                 #
# Purpose: This function calculates the current age #
#          for the contact birthdate passed in      #
#####################################################
def get_age(current, birth):
    current_dates = current.split('/')
    birth_dates = birth.split('/')

    # Convert parts of the dates to integers for calculations
    for i in range(3):
        current_dates[i] = int(current_dates[i])
        birth_dates[i] = int(birth_dates[i])

    # Calculate the age assuming the current
    # birthdate has already happened
    age = current_dates[2] - birth_dates[2]

    # Check to see if the birthdate has not happened yet
    if current_dates[0] < birth_dates[0]:
        age -= 1
    elif current_dates[0] == birth_dates[0]:
        if current_dates[1] < birth_dates[1]:
            age -= 1

    return age

##################################################
# Function name: find_season                     #
# Input: birthdate string in the format m/d/yyyy #
# Output: season as an integer                   #
# Purpose: This function gets the season of the  #
#          birth month passed in                 #
##################################################
def find_season(birthdate):
    
    # Get the month from the birthdate string
    dates = birthdate.split('/')
    month = int(dates[0])
    
    # Decide which season the month is in
    # 12, 1, 2 = winter
    # 3, 4, 5 = spring
    # 6, 7, 8 = summer
    # 9, 10, 11 = fall
    if month <= 2 or month == 12:
        season = "winter"
    elif month <= 5:
        season = "spring"
    elif month <= 8:
        season = "summer"
    else:
        season = "fall"

    # Return the season
    return season

##################################################
# Function name: is_leap_year                    #
# Input: birthdate string in the format m/d/yyyy #
# Output: true if year is a leap year            #
#         false if it is not                     #
# Purpose: This function determines if a year    #
#          is a leap year or not                 #
##################################################
def is_leap_year(birthdate):
    
    # Get the month from the birthdate string
    dates = birthdate.split('/')
    year = int(dates[2])
    
    # Determine if it is a leap year
    
    # If year is evenly divisible by 4
    # check to see if it is a century year
    if year % 4 == 0:
        # If year is a century year
        # check to see if it is evenly divisible by 400
        if year % 100 == 0:
            # At this point, if year is evenly divisible
            # by 400 it is a leap year
            if year % 400 == 0:
                leap_year = True
            else:
                # Century year that is not evenly 
                # divisible by 400 is not a leap year
                leap_year = False
        else:
            # A year evenly divisible by 4 that is
            # not a century year is a leap year
            leap_year = True
    else:
        # A year that is not evenly 
        # divisible by 4 is not a leap year
        leap_year = False

    return leap_year
    

main()
