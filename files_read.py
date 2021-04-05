##  Study of Chapter 6 Files and Exeptions
##  Better late than never.  I will do much better on this Exam 2
##  than I did on Exam 1. Conquer this and RULE my mind.


#   This program reads and displays the contents of 
#   of the prophets.txt file

def main():
    #   Open a file named prophets.txt.
    infile = open('prophets.txt', 'r')

    #   Read the file's content.
    file_contents = infile.read()

    #   Close the file.
    infile.close()

    #   Print the data that was read into memory
    print(file_contents)

main()

