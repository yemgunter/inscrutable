## Ch 7 Lists and Tuples

# List of integers

##even_numbers = [2, 4, 6, 8, 10]
##
##numbers = list(range(1, 10, 2))
##
##print(numbers)


##numbers = [0] * 5
##print(numbers)
##
##
##
##numbers = [99, 100, 101, 102]
##for n in numbers:
##    print(n)
##
##

my_list = [10, 20, 30, 40]

##print(my_list[0], my_list[1], my_list[2], my_list[3])
##
##index = 0
##while index < 4:
##    print(my_list[index], '\n')
##    index += 1

##my_list = [10, 20, 30, 40]
##print(my_list[-1], my_list[-2], my_list[-3], my_list[-4])


# This code will cause an IndexError exception.
my_list = [10, 20, 30, 40]
index = 0
while index < 5:
    print(my_list[index])
    index += 1
