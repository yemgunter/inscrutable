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
      
            for i in birthdates:
                season = find_season(i)
                print(season)
            for i in birthdates:
                year = is_leap_year(i)
                print(year)
            name = contacts.readline()
    
        
        # Close the file 
        contacts.close()

        # Call find_season
        #season = find_season(birthdates)

        # Call is_leap_year
        #year = is_leap_year(birthdates)

        # Call get_age
        #age = get_age(date, birthdates)

        # Call display_contacts
        #display_contacts(names, birthdates)

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
    birthyear = birthdates.split("/")
    birthyear = int(birthyear[2])
            
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

def get_age(date, birthdates):
    today = date.split('/')
    todayMonth = int(today[0])
    todayDay = int(today[1])
    todayYear = int(today[2])
                    
    
    birthyear = birthdates.split('/')
    birthMonth = int(birthyear[0])
    birthDay = int(birthyear[1])
    birthyear = int(birthyear[2])

    if todayMonth > birthMonth:
        age = todayYear - birthyear-1
    else:
        age = todayYear - birthyear
    return age
    

###############################################
# Function name: display_contacts
# Input: name and birthdate lists
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################


          


# Call the main function
main()
