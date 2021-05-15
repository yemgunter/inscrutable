def main():
    month_tuple = (" ", "January", "February", "March", "April",
                   "May", "June", "July", "August", "September",
                   "October", "November", "December")
    birthdate = input("Enter date in format mm/dd/yyyy: ")

    date_list = birthdate.split('/')

    print(month_tuple[int(date_list[0])], " ", date_list[1], ", ",
          date_list[2], sep='')


## Version 1   
    month_entered = int(date_list[0])

    if month_entered == 1:
        month = "January"
    elif month_entered == 2:
        month = "February"
    elif month_entered == 3:
        month = "March"
    elif month_entered == 4:
        month = "April"
    elif month_entered == 5:
        month = "May"
    elif month_entered == 6:
        month = "June"
    elif month_entered == 7:
        month = "July"
    elif month_entered == 8:
        month = "August"
    elif month_entered == 9:
        month = "September"
    elif month_entered == 10:
        month = "October"
    elif month_entered == 11:
        month = "November"
    elif month_entered == 12:
        month = "December"

    print(month, " ", date_list[1], ", ", date_list[2], sep='')
        

 
main()
