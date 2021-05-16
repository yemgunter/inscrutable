class Contact:

    # sets name and birthdate to an empty string – “”
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

    def find_season(self):
        space = self.get_birthdate().index(" ")
        month = self.get_birthdate()[:space]

        if month == "December" or \
           month == "January" or \
           month == "February":
            season = "winter"
        elif month == "March" or \
             month == "April" or \
             month == "May":
            season = "spring"
        elif month == "June" or \
             month == "July" or \
             month == "August":
            season = "summer"
        elif month == "September" or \
             month == "October" or \
             month == "November":
            season = "fall"
        return season

    def calculate_age(self, todays):
        todays_date = int(todays[-4:])
        birth_dates = int(self.get_birthdate()[-4:])
                                           
        for i in range(todays_date, birth_dates):
            todays_date = int(todays_date)
            birth_dates = int(birth_dates)

        age = todays_date - birth_dates
        
        return age

    def is_leap_year(self):
        birthyear = int(self.get_birthdate()[-4:])
        
        if birthyear % 4 == 0 and birthyear % 100 != 0 or \
        birthyear % 400 == 0:
            year = "Yes"
        else:
            year = "No"
        return year
        
        

    def __str__(self):
        return "Name: " + self.__name + '\n' + \
               "Age: " + self.__birthdate + '\n' + \
               "Season: " + self.__name + '\n' + \
               "Leap Year?: " + self.__birthdate
