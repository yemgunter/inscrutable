##  Study of Chapter 6 Files and Exeptions
##  Better late than never.  I will do much better on this Exam 2
##  than I did on Exam 1. Conquer this and RULE my mind.


#   This program gets three names from the user
#   and writes them to a file

def main():
    #  Open a file named friends.txt.
    infile = open('prophets.txt', 'w')

    #   Read three lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #  Strip the \n from each string
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    #   Close the file.
    infile.close()

    #   Print the data that was read into memory
    print(line1)
    print(line2)
    print(line3)
 
# Call the main function.
main()

