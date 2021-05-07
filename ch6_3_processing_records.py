# chapter 6 reboot 5/2/21 Saturday to beat Lab 4 to death
# replay lectures from 3/30 Tuesday


# 6.4 this program will read the file,
# establish records out of the file then process them

import os

def main():
    try:
        friends = open('friends2.txt', 'r') #open the file
        temp_file = open('temp.txt', 'w')   #create file of still friends

        friend_remove = input("Enter name of friend to remove: ")

        name = friends.readline()  # read first line name field
        while name != "":  #if a field is read establish records
            name = name.rstrip('\n')   #strip \n from name field
            age = int(friends.readline()) #convert string age to interger
            food = friends.readline().rstrip('\n')  #strip \n from food field

            print(name, age, food) #diplay record
            if name != friend_remove:  #check if its NOT the friend
                temp_file.write(name + '\n')
                temp_file.write(str(age) + '\n')
                temp_file.write(food + '\n')

            name = friends.readline() #read name field of next record

        friends.close()
        temp_file.close()

        #remove file then rename it
        os.remove('friends2.txt')
        os.rename('temp.txt', 'friends2.txt')

    #file not found exception
    except FileNotFoundError: 
        print("File was not found") 
    except Exception as err:
        print("Error:", err)
    
main()
    



