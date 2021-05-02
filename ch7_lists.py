# chapter 7 reboot 5/2/21 Sunday to beat Lab 4 to death
# replay lectures from 4/8 Thursday


# 7.1 - 7.2  Lists, accessing elist lements using index & range

def main():
    list1 = [1, 2, 3]

    list2 = list(range(9)) #generates a list with sequence 0-8

    list3 = [0] * 20 # using * repetition operator

    list4 = list1 + list2 #oncatenates the lists

    print(list1)
    print(list2)
    print(list3)
    print(list4)

    print("List 4 is:")
    #use for loop to process a list
    for i in range(len(list4)):
        print(list4[i])





    
##    things = [43, "Jimmy", 9.3, True]
##    
##    for i in range(4):
##        print( i+1, ". ", things[i], sep='')
##
##    print()  #print blank line between list
##
##    
##    for i in range(1,5):
##        print( i, ". ", things[i-1], sep='')
##
##    print()  #print blank line between list sets
##    
##    
##    for value in things:
##        print(value)


    

    #create list & access each indexed element in the list
#   item_numbers = ["R4G", "83J", "Qw34", "8332", "M9"]
#
#   #which one do i want to access?
#   for i in range (5):
#       print(item_numbers[i])
#
#
#   print(item_numbers)





main()


