###############################################################
# Yolanda Gunter
#  Lab 4             
# My program uses decisions, repetition, functions, files, lists
# and exception handling that will get the input from a file to
# run program that asks User for current date, reads a contact file
# list taht contains names with DOB, calculate each contact's age,
# season contact was born in and if they were born in a leap year or not.
# Then my program will print the output of the information with the
# calculated average age of contacts in the data file.
###############################################################


########################################################
# Function name: main
# Input: None
# Output: print User's greeting, birth season & if leap yr or not 
# Purpose: This function reads a data file of contacts with DOB, then prints
# a table of each contact's name, age, season born in and if they were born
# in a leap year or not with a separate line printed of the
# calculated average age of contacts in the data file.
###############################################
def main():

        # Create empty name list
    name = []

    # Create empty birthdate list
    birthdate = []

    
        try:
            
            # Open a file named contactlab4.txt
            infile = open('contactsLab4.txt', 'r')

            # Read first record's name field
            name = infile.readlines()
            # Read rest of the file
            while name != '':
                nlist
                # Read the birthdate field
                birthdate = infile.read()
                date_list = birthdate.split('/')
                
            # Strip the \n from name
            name = name.rstrip('\n')

            
    
            # Call the find_season function
            season = find_season(month_tuple)
            
            # Call the is_leap_year funcion
            year = is_leap_year(birthdate)
            date_list = birthdate.split('/')

            # Call the get_age function

            age = get_age(date)
            today = date.split('/')
                
            # Call the display_contacts functions
            display_contacts(name, birthdate)

            

# Close the file 
            infile.close()
        except IOError:
            print('An error occured trying to read')
            print('the file', infile)           

            date = int(input('Enter current date in format ' \
                               'm/d/yyyy or Enter end to stop: ')) 
###############################################
# Function name: find_season
# Input: birthdate
# Output: a string as a season
# Purpose: Determines which season contact is born 
###############################################

def find_season(month_tuple):
    # Assign contact birth month to a season
    month_tuple = date_list[0]
    if month_tuple == 12 or month_tuple == 1 or month_tuple == 2:
        season = "winter"
    elif month_tuple == 3 or month_tuple == 4 or month_tuple == 5:
        season = "spring"
    elif month_tuple == 6 or month_tuple == 7 or month_tuple == 8:
        season = "summer"
    elif month_tuple == 9 or month_tuple == 10 or month_tuple == 11:
        season = "fall"
    return season
    
    

###############################################
# Function name: is_leap_year
# Input: birthdate 
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################
def is_leap_year(birthdate):
    date_list = birthdate.split('/')
    year = date_list[int(birth_date[2])]
            
    # Calculate if User's birth year is a leap year or not
    if birthdate % 4 == 0 and birthdate % 100 != 0 or \
    birthdate % 400 == 0:
        year = "Yes"
    else:
        year = "No"
    return year

###############################################
# Function name: get_age
# Input: None
# Output: age of contact 
# Purpose: Caculates age of contact    
###############################################
def get_age(date):
    date -= birthdate[2]
    

###############################################
# Function name: display_contacts
# Input: birth_year
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################
def display_contacts(name, birthdate):
    for name in 

    
            
    

# Call the main function
main()
