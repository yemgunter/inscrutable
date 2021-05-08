
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
            birthdate = contacts.readline()
            birthdates.append(birthdate.rstrip('\n'))
            
            name = contacts.readline()
    
        
        # Close the file 
        contacts.close()

        # Call get_age
        display_contacts(names, birthdates)

    # Simple exception if file is not found
    except FileNotFoundError:
        print("File was not found")
    except Exception as err:
        print("Error:", err)
            


###############################################
# Function name: get_age
# Input: current date and birthdate list
# Output: age of contact 
# Purpose: Caculates age of contact    
###############################################

def get_age(birthdates, todays):
    birthyear = birthdates.split('/', 3)
    birthyear = int(birthyear[2])
    birthDay = int(birthyear[1])
    birthMonth = int(birthyear[0])

    today = todays.split('/', 3)
    todayYear = int(today[2])
    todayDay= int(today[1])
    todayMonth = int(today[0])
    
    
    if todayMonth > birthMonth:
        age = todayYear - birthyear
    elif todayMonth == birthMonth \
         and todayDay > birthDay:
        age = todayYear - birthyear
    else:
        age = todayYear - birthyear - 1
    return age


###############################################
# Function name: display_contacts
# Input: name and birthdate lists
# Output: value leap year (Yes) or not (No) 
# Purpose: Determines if birth year is leap year or not.    
###############################################
def display_contacts(names, birthdates):
    
    # Get current date
    todays = input('Enter current date in format m/d/yyyy: ')
    

    # format display in table format with column headings
    print(format("Name", '25'), format("Age", '6'))
    print(format("----", '25'), format("---", '6'))
    for i in range(len(names)):
        print(format(names[i], '25'), \
              format(str(get_age(birthdates, todays[i])), '10'))
  

# Call the main function
main()
