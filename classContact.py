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

    def __str__(self):
        return "Name: " + self.__name + '\n' + \
               "Birthdate: " + self.__birthdate
