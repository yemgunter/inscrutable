###############################################################
# Yolanda Gunter
#  Lab 1             
# My program will ask for User's name, birth month and birth year
# then tell User what season they were born in and
# if they were born in a leap year or not. 
###############################################################



## Final Print should be
## The user enters their name is “Jim Pembry”
## and they were born in the month “6” and the year 1971.
## Your program should display this exact message:
## Hello, Jim Pembry! You were born in the summer and 1971 was not a leap year.


# Get User's name
first_name = input('Enter your first name: ')


# Get User's birth month as interger
birth_season = int(input('Enter your birth month number Ex: January = 1: '))

# Get User's birth year
birth_year = int(input('Enter your birth year Ex: 1986: '))

# Display greeting to User, season of birth and if birth year was leap or not

print("Hello, ", first_name, "! You were born in the ", birth_season, " and ",
      birth_year, " was not a leap year.
