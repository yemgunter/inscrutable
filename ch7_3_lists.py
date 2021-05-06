# chapter 7 reboot 5/5/21 Sunday to beat Lab 4 to death
# replay lectures from 4/13 Tuesday


def main():

    #create empty list
    int_list = []
    
    input_file = open("numbers2.txt", 'r')

    for line in input_file:
        int_list.append(int(line))

    print(int_list)
    
        
    input_file.close()



main()

# use concatenation for lists
# list1 = [1, 2, 3]
# list2 = list1 + [3, 4, 5]

##    numbers_list = [1, 2, 3, 4, 5]
##
##    middle = numbers_list[1:4]
##    list1 = numbers_list[2:10]
##    #print(list1)
##
##    # start at end of list from -3 to end
##    list3 = numbers_list[-3:]
##    print(list3)
    

##    list2 = numbers_list[0:5:2]
##    print(list2)

##    print(numbers_list)
##    print(middle)



