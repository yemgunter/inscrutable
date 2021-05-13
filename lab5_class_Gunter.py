#############################################################
# Yolanda Gunter
# Lab 5 - Define the Contact class
#   Data attributes:
#       name - string
#       birthdate - string
#   Methods:
#      __init__  – sets name and birthdate to an empty string – “”
#      set_name(string contact_name)
#      get_name() – returns a string
#      set_birthdate(string contact_birthdate)
#      get_birthdate() – returns a string
#      find_season() – returns a string
#      is_leap_year() – returns the boolean value true or false
#      calculate_age() – return an integer
##############################################################

class Contact:

    # initialize the attributes
    def __init__(self, name='', birthdate=''):
        self.__name = name
        self.__birthdate = birthdate

    # assessor methods
    def get_name(self):
        return self.__name
    
    def get_birthdate(self):
        return self.__birthdate
    
    # mutator methods
    def set_name(self, contact_name):
        self.__name = contact_name
        
    def set_birthdate(self, contact_birthdate):
        self.__birthdate = contact_birthdate


##    # Method calculate age
##    def calculate_age(current, birth):
##        current_dates = current.split('/')
##        birth_dates = birth.split('/')
##
##        # convert parts from the dates to integers for calculations
##        for i in range(3):
##            current_dates[i] = int(current_dates[i])
##            birth_dates[i] = int(birth_dates[i])
##
##        # calculate the age assumeing the current birthdate
##        # has already happened
##        age = current_dates[2] - birth_dates[2]
##
##        # check to see if the birthdate has not happened yet
##        if current_dates[0] < birth_dates[0]:
##            age -= 1
##        elif current_dates[0] == birth_dates[0]:
##            if current_dates[1] < birth_dates[1]:
##                age -= 1
##
##        return age


    # Method name: find_season
    def find_season(self):
        # isolates month element of birthdate string
        space = self.get_birthdate().index(" ")
        month = self.get_birthdate()[:space]
        months = (" ", "January", "February", "March", "April",
                   "May", "June", "July", "August", "September",
                   "October", "November", "December") 
       
        # Assign contact birth month to a season
        if months == months[12] or \
           month == months[1] or \
           month == months[2]:
            season = "winter"
        elif month == months[3] or \
             month == months[4] or \
             month == months[5]:
            season = "spring"
        elif month == months[6] or \
             month == months[7] or \
             month == months[8]:
            season = "summer"
        elif month == months[9] or \
             month == months[10] or \
             month == months[11]:
            season = "fall"
        return season
        
    # Method name: is_leap_year
    def is_leap_year(self):
        # isolates month element of birthdate string
                
        # Calculate if User's birth year is a leap year or not
        if birthyear % 4 == 0 and birthyear % 100 != 0 or \
        birthyear % 400 == 0:
            year = "Yes"
        else:
            year = "No"
        return year


    def __str__(self):
        return "Name: " + self.__name + '\n' + \
               "Birthdate: " + self.__birthdate
        
        

