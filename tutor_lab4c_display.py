###############################################################
# Yolanda Gunter
#  Lab 4             
# My program uses decisions, repetition, functions, files, lists
# and exception handling that will get the input from a file to
# run program that asks User for current date, reads a contact file
# list that contains names with DOB, calculate each contact's age,
# season born in and born in a leap year or not.
# Then my program will print the calculated average age of contacts.
###############################################################


########################################################
# Function name: main
# Input: contactsLab4.txt file
# Output: table of contact, age, birth season & if born leap yr or not 
# Purpose: This function reads file, makes two lists, converts strings to 
# integers, calculates ages, season born & if born leap yr or not 
# then lastly calculats average age of contacts in entire file.
###############################################
def main():

    # start exception handling
    try:

        # Open a file named contactlab4.txt
        contacts = open('contactsLab4.txt', 'r')

        # Create empty name list
        names = []

        # Create empty birthday list
        birthdates = []

        # Read file, establish records, strip \n, append to lists, 
        name = contacts.readline()
        while name != '':
            names.append(name.rstrip('\n'))
            date = contacts.readline()
            birthdates.append(date.rstrip('\n'))
            
            name = contacts.readline()
    
        
        # Close the file 
        contacts.close()

        # Call display_contacts
        display_contacts(names, birthdates)

    # Simple exception if file is not found
    except FileNotFoundError:
        print("File was not found")
    except Exception as err:
        print("Error:", err)
            

###############################################
# Function name: find_season
# Input: birthdate
# Output: a string as a season
# Purpose: Determines which season contact is born 
###############################################

def find_season(birthdates):
    month = birthdates.split("/", 3)
    month = int(month[0])
    
    # Assign contact birth month to a season
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
# Input: birthdate list
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################

def is_leap_year(birthdates):
    birthyear = birthdates.split('/')
    birthyear = [int(birthyear[2])]
            
    # Calculate if User's birth year is a leap year or not
    if birthyear % 4 == 0 and birthyear % 100 != 0 or \
    birthyear % 400 == 0:
        year = "Yes"
    else:
        year = "No"
    return year

###############################################
# Function name: get_age
# Input: birthdate list
# Output: age of contact 
# Purpose: Caculates age of contact    
###############################################

##def get_age(date, birthdate):
##    date -= birthdate[2]
    

###############################################
# Function name: display_contacts
# Input: name and birthdate lists
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################
def display_contacts(names, birthdates):
    # Get current date
    date = input('Enter current date in format m/d/yyyy: ')

    # format display in table format with column headings
    print(format("Name", '25'), format("Age", '4'),
          format("Season", '8'), format("Leap Year", '10'))
    print(format("----", '25'), format("---", '4'),
          format("------", '8'), format("---------", '10'))
    for i in birthdates:
        season = find_season(i)      
    for i in birthdates:
        year = is_leap_year(i)
    for i in range(len(name)):
        print(format(name[i], '25'), format(birthdates[i], '10'),
              format(season[i], '8'), format(year[i], '10'))

# Call the main function
main()
