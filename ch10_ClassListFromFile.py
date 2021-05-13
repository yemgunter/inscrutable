import ch10FriendClass

def main():
    friends_file = open("friends2.txt", 'r')
    friend_list = []

    name = friends_file.readline()
    while name != "":
        name = name.rstrip('\n')       
        age = int(friends_file.readline())        
        food = friends_file.readline().rstrip('\n')
        a_friend = ch10FriendClass.Friend(name, age, food)
        friend_list.append(a_friend)
        
        name = friends_file.readline()
    
    friends_file.close()

    display_friends(friend_list)
    print()

    print("Now let's add a friend")
    name = input("Enter their name ")
    age = int(input("Enter age "))
    food = input("What is their favorite food? ")
    new_friend = ch10FriendClass.Friend(name, age, food)
    friend_list.append(new_friend)

    print()
    display_friends(friend_list)
    
    
def display_friends(chums):           
    print(format("Name", '20'), format("Age", '5'),
          format("Favorite food", '25'))
    for i in range(len(chums)): 
        print(format(chums[i].get_name(), '20'),
              format(str(chums[i].get_age()), '5'),
              format(chums[i].get_food(), '25'))

main()



