###############################################################
# Yolanda Gunter
#  Lab 3
# My program uses decisions, repetition and functions that will ask
# for User's name, birth month and birth year to run program that
# greet User with what season they were born in and if they were
# born in a leap year or not. Then my program will ask for how many
# pennies they have in their penny jar and calculate and display
# the number of each money denomination they will get when they cash them in.
#
###############################################################


########################################################
# Function name: main
# Input: passes to first_name, birth_month, birth_year
# Output: print User's greeting, birth season & if leap yr or not
# Purpose: This function greets User with what season they were
# born in and if they were born in a leap year or not.
###############################################
def main():

    # Get User's name
    first_name = input('Enter your first name: ')

    # Call the get_month function
    month = get_month()
    
    # Call the get_year function
    birth_year = get_year()
    
    # Call the find_season function
    season = find_season(month)
    
    # Call the is_leap_year funcion
    year = is_leap_year(birth_year)
    
    # Display greeting to User, season of birth and
    # if birth year was leap or not
    print("Hello, ", first_name, "! You were born in the ", season, " and ",
          birth_year, " was ", year, sep='')


###############################################
# Function name: get_month
# Input: month
# Output: the valid month as an integer between 1 and 12
# Purpose: This function validates input and stores as month
###############################################

def get_month():
    month = int(input('Enter numeric birth month between 1 and 12: '))
    # Validate the month entered
    while month < 1 or month > 12:
        print('ERROR: Month must be between 1 and 12')
        month = int(input('Enter a valid month between 1 and 12: '))
    return month

###############################################
# Function name: get_year
# Input: Describe values passed on the parameter list
# Output: Describe the value(s) returned
# Purpose: This function does this…
###############################################

def get_year():
    birth_year = int(input('Enter valid birth year Ex: 1986: '))
    # Validate the year entered
    while birth_year < 0 or birth_year == 0:
        print('ERROR: Year cannot be 0')
        birth_year = int(input('Enter valid birth year Ex: 1986: '))
    return birth_year


###############################################
# Function name: find_season
# Input: the month
# Output: string value of the corresponding season
# Purpose: This function determines which season
# User is born in based month
###############################################

def find_season(month):
    # Assign User's birth month to a season 
    if month == 12 or month == 1 or month == 2:
        season = "winter"
    elif month == 3 or month == 4 or month == 5:
        season = "spring"
    elif month == 6 or month == 7 or month == 8:
        season = "summer"
    elif month == 9 or month == 10 or month == 11:
        season = "fall"
    return season


###############################################
# Function name: is_leap_year
# Input: Describe values passed on the parameter list
# Output: Describe the value(s) returned
# Purpose: This function does this…
###############################################

def is_leap_year(birth_year):
    # Calculate if User's birth year is a leap year or not
    if birth_year % 4 == 0 and birth_year % 100 != 0 or \
       birth_year % 400 == 0:
        status = 'leap year.' 
    else:
        status = 'not a leap year.'
    return status

###############################################
# Function name: penny_jar
# Input: Describe values passed on the parameter list
# Output: Describe the value(s) returned
# Purpose: This function does this…
###############################################



# Call the main function
main()
