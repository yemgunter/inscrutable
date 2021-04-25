##############################################################
# Lab 3 Solution                                             #
# This program reads the user's name, birth month and year.  #
# It will tell them what season they were born and if the    #
# year was a leap year or not.                               #
# Then the program will ask the user for their yearly salary #
# and display it in terms of monthly, daily and hourly       #
# amounts.                                                   #
# The program will contine to let the user enter names,      #
# birthdate info and salary until they are done. They will   #
# enter a name of "zzz" to signal they are done.             #
#############################################################

def main():
    # Priming read for the sentinel-controlled while loop
    # Read the first user's name or "zzz" to quit
    name = input('Enter your name or "zzz" to quit: ')

    # Check for the sentinal value of "zzz"
    while name != "zzz":
        # Get the user's birth month
        birth_month = get_month()

        # Get the user's birth year
        birth_year = get_year()

        # Get the season
        season = find_season(birth_month)

        # Call function to determine if the year was a leap year or not
        if is_leap_year(birth_year):
            leap_year = ' was a leap year'
        else:
            leap_year = ' was not a leap year'
            
        # Display message to the user
        print("\nHello, ", name, "! You were born in the ", season,
              " and ", birth_year, leap_year, '.', sep='')
        print()

        pennies = int(input("How many pennies are in your penny jar? "))
        penny_jar(pennies)
        

        # Update read for the sentinel-controlled while loop
        # Read the next user's name or "zzz" to quit
        name = input('\nEnter your name or "zzz" to quit: ')

################################################
# Function name: get_month                     #
# Input: none                                  #
# Output: month as an integer                  #
# Purpose: This function gets the month in     #
#          which the user was born             #
################################################
def get_month():
    # Read user's birth month and validate it
    month = int(input("Enter the month you were born as an integer: "))
    while month < 1 or month > 12:
        print("Invalid month: must be between 1 and 12")
        month = int(input("Enter the month you were born as an integer: "))
    # Return the valid month
    return month

################################################
# Function name: get_year                      #
# Input: none                                  #
# Output: year as an integer                   #
# Purpose: This function gets the year in      #
#          which the user was born             #
################################################
def get_year():       
    # Read user's birth year and validate it
    year = int(input("Enter the year you were born (yyyy): "))
    while year <= 0:
        print("Invalid year: must be greater than zero")
        year = int(input("Enter the year you were born (yyyy): "))
    # Return the valid year
    return year

################################################
# Function name: find_season                   #
# Input: month as an integer                   #
# Output: season as an integer                 #
# Purpose: This function gets the season the   #
#          month is in                         #
################################################
def find_season(month):
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

################################################
# Function name: is_leap_year                  #
# Input: year as an integer                    #
# Output: true if year is a leap year          #
#         false if it is not                   #
# Purpose: This function determines if a year  #
#          is a leap year or not               #
################################################
def is_leap_year(year):
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

##################################################
# Function name: penny_jar                       #
# Input: number of pennies                       #
# Output: none                                   #
# Purpose: This function calculates the number   #
#          of dollars, quarters, dimes, nickels  #
#          and pennies they will get when they   #
#          cash in the pennies                   #
##################################################
def penny_jar(total_pennies):

    # Preserve the original total penny amount
    pennies = total_pennies
    # Calculate dollars
    dollars = pennies // 100
    # Subtract out the dollars from the pennies
    pennies = pennies - (dollars * 100)

    # Calculate quarters
    quarters = pennies // 25
    # Subtract out the quarters from pennies
    pennies = pennies - (quarters * 25)

    # Calculate dimes
    dimes = pennies // 10
    # Subtract out the dimes from pennies
    pennies = pennies - (dimes * 10)

    # Calculate nickels
    nickels = pennies // 5
    # Subtract out the nickels from pennies
    pennies = pennies - (nickels * 5)

    # Display the amount in denominations
    print(total_pennies, " pennies comes to the following:")
    print("\tdollars: ", dollars)
    print("\tquarters: ", quarters)
    print("\tdimes: ", dimes)
    print("\tnickels: ", nickels)
    print("\tpennies: ", pennies)
    

main()
