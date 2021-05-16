import classContact

def main():
    try:
        friends_file = open("contactsLab5.txt", 'r')
        friend_list = []

        name = friends_file.readline()
        while name != "":
            name = name.rstrip('\n')       
            birthdate = friends_file.readline().rstrip('\n')     
            a_friend = classContact.Contact(name, birthdate)
            friend_list.append(a_friend)
            
            name = friends_file.readline()
        
        friends_file.close()
     
        display_friends(friend_list)
    except FileNotFoundError:
        print("File was not found")
    except Exception as err:
        print("Error:", err)

        
    
def display_friends(chums):
    # Get current date
    todays = input("Enter current date in the format 'month d, yyyy': ")

    # initiates total age to use in average age calculation
    total_age = 0

    
    print(format("Name", '20'), format("Age", '7'),
          format("Season", '10'), format("Leap Year?", '5'))
    print(format("----------", '20'), format("-----", '7'),
          format("------", '10'), format("---------", '5'))
    for i in range(len(chums)):

        ages = int(chums[i].calculate_age(todays))

        total_age += ages
        
        print(format(chums[i].get_name(), '20'), \
              format(str(chums[i].calculate_age(todays)), '7'), \
              format(chums[i].find_season(), '10'), \
              format(chums[i].is_leap_year(), '5'))
    
    print("\nAverage age of contact is ", total_age // len(chums))

    
main()



