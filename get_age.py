def get_age(birthdates, currentDate):
    birthdate = birthdates
    
    birthdate_list = birthdate.split('/')
    currentDate_list = currentDate.split('/')

    
    birthdate_year = int(birthdate_list[2])
    currentDate_year = int(currentDate_list[2])
    
    birthdate_month = int(birthdate_list[0])
    currentDate_month = int(currentDate_list[0])
    
    birthdate_day = int(birthdate_list[1])
    currentDate_day = int(currentDate_list[1])
    
    if currentDate_month > birthdate_month: 
        age = currentDate_year - birthdate_year
        
    elif currentDate_month == birthdate_month \
         and currentDate_day > birthdate_day:
        age = currentDate_year - birthdate_year
    else:
        age = currentDate_year - birthdate_year - 1
    return age
