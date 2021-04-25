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
# Input: None
# Output: print User's greeting, birth season & if leap yr or not 
# Purpose: This function greets User with what season they were 
# born in and if they were born in a leap year or not.    
###############################################
def main():
    
    # Get User's name
    first_name = input('Enter your first name: ')
    while first_name != 'zzz':

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
        print("Hello, ", first_name, "! You were born in the ",
              season, " and ", birth_year, " was ", year, sep='')

        # Get User's number of pennies in their penny jar
        amount = int(input('How many pennies are in your penny jar?: '))
        
        # Call the penny_jar function
        penny_jar(amount)

        first_name = input('Enter another first name or ' \
                           'Enter zzz to stop: ')

###############################################
# Function name: get_month
# Input: None
# Output: value returned as month
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
# Input: None
# Output: User's birth year
# Purpose: This function validates input and stores as year    
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
# Input: month
# Output: season
# Purpose: Determines which season User is born 
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
# Input: User's birth year
# Output: value leap year (true) or not (False) 
# Purpose: Determines if birth year is leap year or not.    
###############################################

def is_leap_year(birth_year):
    # Calculate if User's birth year is a leap year or not
    if birth_year % 4 == 0 and birth_year % 100 != 0 or \
       birth_year % 400 == 0:
        year = "a leap yaer."
    else:
        year = "not a leap year."
    return year

###############################################
# Function name: penny_jar
# Input: User's amount
# Output: None
# Purpose: Calculate and display the number of each money
# denomination    
###############################################

def penny_jar(amount):
    # Calculate and display the number of each money denomination
    print(amount // 100, "dollars")
    amount %= 100
    print(amount // 25, "quarters")
    amount %= 25
    print(amount // 10, "dimes")
    amount %= 10
    print(amount // 5, "nickles")
    amount %= 5
    print(amount//1, "pennies")


# Call the main function
main()
