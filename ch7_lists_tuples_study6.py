## Ch 7 Lists and Tuples


## Copying Lists  Ch 7.6


# Create a list with values.
##list1 = [1, 2, 3, 4]
### Create an empty list.
##list2 = []
### Copy the elements of list1 to list2.
##for item in list1:
##    list2.append(item)


# Create a list with values.
list1 = [9, 11, 13, 15]
print(list1)
# Add list1 to the beginning of list2.
list2 = list1 + [17, 19, 21, 23]
print(list2)
# Add list2 to the end of list3 below. 
list3 = [1, 3, 5, 7] + list2
print (list3)
