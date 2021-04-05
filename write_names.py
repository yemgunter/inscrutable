##  Study of Chapter 6 Files and Exeptions
##  Better late than never.  I will do much better on this Exam 2
##  than I did on Exam 1. Conquer this and RULE my mind.


#   This program gets three names from the user
#   and writes them to a file

def main():
    #   Get three names
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    #  Open a file named friends.txt.
    myfile = open('friends.txt', 'w')

    #  Write the names to the file.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    #   Close the file.
    myfile.close()

    #   Print the data that was read into memory
    print('The names were written to friends.txt.')
 
# Call the main function.
main()

