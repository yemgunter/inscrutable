import Contact

def main():
    friends_file = open("friends2.txt", 'r')
    friend_list = []

    name = friends_file.readline()
    while name != "":
        name = name.rstrip('\n')       
        birthdate = friends_file.readline.rstrip('\n')      
        a_friend = classContact.Friend(name, birthdate)
        friend_list.append(a_friend)
        
        name = friends_file.readline()
    
    friends_file.close()

    print(name[0:2])
    print(birthdate[:2])
    print(names[2:])
    print(name[:])
    display_friends(friend_list)
    
    
def display_friends(chums):           
    print(format("Name", '20'), format("Age", '5'),
          format("Birthdate", '25'))
    for i in range(len(chums)): 
        print(format(chums[i].get_name(), '20'),
              format(str(chums[i].get_birthdate()), '5')

main()



