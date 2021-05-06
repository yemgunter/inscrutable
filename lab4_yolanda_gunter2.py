###############################################################
# Yolanda Gunter
#  Lab 4             
# My program uses decisions, repetition, functions, files, lists
# and exception handling that will get the input from a file to
# run program that asks User for current date, reads a contact file
# list that contains names with DOB, calculate each contact's age,
# season born in and born in a leap year or not.
# Then my program will print the calculated average age.
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

    try:

        name = []
        birthdate = []
        
        # Open a file named contactlab4.txt
        contacts = open('contactsLab4.txt', 'r')
        

        # Read files, make lists, strip \n and establish records
        for line in contacts:
            name.append(int(line))

        for value in name:
            birthdate.append(value)
            

            print(name, birthdate)   
         
         # Close the file 
        contacts.close()

    # Simple exception if file is not found
    except FileNotFoundError:
        print("File was not found")
    except Exception as err:
        print("Error:", err)



    

    
  
##    # Call the is_leap_year funcion
##    year = is_leap_year(birthdate)
##    date_list = birthdate.split('/')
##
##    # Call the get_age function
##
##    age = get_age(date) today = date.split('/')
##        
##    # Call the display_contacts functions
##    display_contacts(name, birthdate)

            


###############################################
# Function name: find_season
# Input: birthdate
# Output: a string as a season
# Purpose: Determines which season contact is born 
###############################################

##def find_season():
##    date_list = birthdate.split('/')
##    month = date_list[0]
##    
##    # Assign contact birth month to a season
##    if month == 12 or month == 1 or month == 2:
##        season = "winter"
##    elif month == 3 or month == 4 or month == 5:
##        season = "spring"
##    elif month == 6 or month == 7 or month == 8:
##        season = "summer"
##    elif month == 9 or month == 10 or month == 11:
##        season = "fall"
##    return season
    
    

###############################################
# Function name: is_leap_year
# Input: birthdate list
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################

##def is_leap_year(birthdate):
##    date_list = birthdate.split('/')
##    year = date_list[int(birth_date[2])]
##            
##    # Calculate if User's birth year is a leap year or not
##    if birthdate % 4 == 0 and birthdate % 100 != 0 or \
##    birthdate % 400 == 0:
##        year = "Yes"
##    else:
##        year = "No"
##    return year

###############################################
# Function name: get_age
# Input: birthdate list
# Output: age of contact 
# Purpose: Caculates age of contact    
###############################################

##def get_age(date):
##    date -= birthdate[2]
    

###############################################
# Function name: display_contacts
# Input: name and birthdate lists
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################

#def display_contacts(name, birthdate):
   

    
            
    

# Call the main function
main()
