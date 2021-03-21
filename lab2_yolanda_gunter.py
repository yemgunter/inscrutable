###############################################################
# Yolanda Gunter
#  Lab 2             
# My program uses a sentinel controlled while loop that will ask
# for User's name, birth month and birth year. My program's first
# input will process if it is not the sentinel value, will
# validate the entered birth month to be between 1 and 12,
# display an error message if input of birth month is invalid and
# read next input (birth year) if valid utilizing a validation loop.
# Valid inputs will run program that greet User with what season
# they were born in and if they were born in a leap year or not. 
###############################################################


# Get User's name
first_name = input('Enter your first name: ')

# Set sentinel value
while first_name != 'zzz':
# Get User's birth month as interger
    month = int(input('Enter numeric birth month between 1 and 12: '))
    
# Validate the month entered
    while month < 1 or month > 12:
        print('ERROR: Month must be between 1 and 12')
        month = int(input('Enter a valid month between 1 and 12: '))
        
# Assign User's birth month to a season 
    if month == 12 or month == 1 or month == 2:
        season = "winter"
    elif month == 3 or month == 4 or month == 5:
        season = "spring"
    elif month == 6 or month == 7 or month == 8:
        season = "summer"
    elif month == 9 or month == 10 or month == 11:
        season = "fall"

# Get User's birth year
    birth_year = int(input('Enter your birth year Ex: 1986: '))

# Validate the year entered
    while birth_year < 0 or birth_year == 0:
        print('ERROR: Year cannot be 0')
        birth_year = int(input('Enter valid birth year Ex: 1986: '))

# Calculate if User's birth year is a leap year or not
    if birth_year % 4 == 0 and birth_year % 100 != 0 or \
       birth_year % 400 == 0:
        year = "a leap yaer."
    else:
        year = "not a leap year."

# Display greeting to User, season of birth and if birth year was leap or not
    print("Hello, ", first_name, "! You were born in the ", season, " and ",
          birth_year, " was ", year, sep='')
# Do this again?
    first_name = input('Enter another first name or ' \
                       'Enter zzz to stop: ')
