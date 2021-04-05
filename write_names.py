##  Study of Chapter 6 Files and Exeptions
##  Better late than never.  I will do much better on this Exam 2
##  than I did on Exam 1. Conquer this and RULE my mind.


#   This program reads the contents of 
#   of the prophets.txt file one line at a time

def main():
    #   Open a file named prophets.txt.
    infile = open('prophets.txt', 'r')

    #   Read three lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #   Close the file.
    infile.close()

    #   Print the data that was read into memory
    print(line1)
    print(line2)
    print(line3)

main()

