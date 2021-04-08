#### This program writes 100 random numbers to a file
##
##
import random

# Open a file.
myfile = open('numbers.txt', 'w')

# Write 100 random numbers to the file.
for count in range(100):
    number = random.randint(1,100)
    myfile.write(str(number) + '\n')

# Close the file.
myfile.close()
print('Done')



