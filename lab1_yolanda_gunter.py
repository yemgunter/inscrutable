###############################################################
# Yolanda Gunter
#  Lab 1             
# My program will ask for User's name, birth month and birth year
# then greet User with what season they were born in and
# if they were born in a leap year or not. 
###############################################################

# Get User's name
first_name = input('Enter your first name: ')


# Get User's birth month as interger
month = int(input('Enter numeric birth month between 1 and 12: '))

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

# Calculate if User's birth year is a leap year or not
if birth_year % 4 == 0 and birth_year % 100 != 0 or birth_year % 400 == 0:
    year = "a leap yaer."
else:
    year = "not a leap year."


# Display greeting to User, season of birth and if birth year was leap or not

print("Hello, ", first_name, "! You were born in the ", season, " and ",
      birth_year, " was ", year, sep='')
