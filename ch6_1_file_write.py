# chapter 6 reboot 5/1/21 Saturday to beat Lab 4 to death
# replay lectures from 3/25 Thursday


def main():



############## Create, Write and Append to file ##########
##    names_out = open("names.txt", 'a')
##
##    # Add names to file then appended these names to the file
####    names_out.write("Min. Artramease\n")
####    names_out.write("Gorgeous Gunter\n")
####    names_out.write("DJ Tuki\n")
##
##    # Input name from User to the file
##    name = input("Enter a name: ")
##    names_out.write(name + "\n") # Pass name and contatenate \n 
##
##    names_out.close()


################ Read fron file Strings  ##########
##    
##    names_in = open("names.txt", 'r')
##
##    name1 = names_in.readline().rstrip('\n') # one step rstrip
##    print(name1)
##    name2 = names_in.readline() # two step rstrip
##    name2 = name2.rstrip('\n')
##    print(name2)
##
##    names_in.close()


################ Read fron file Numbers (integers)  ##########
##
##    infile = open("numbers2.txt", 'r') #open file
##
##    value = infile.readline()  #read line
##    while value != '':  #while we are not at end of the line
##        value = int(value) #convert value to interger
##        print(value*2) #display value times 2
##        value = infile.readline()  #read the next line
##
##    
##
##
################ Write Even Numbers To File(integers)  ##########
##    
##    infile = open("numbers2.txt", 'w') #open file
##
##    even = int(input("How many numbers? "))
##
##    for i in range(even):  
##        num = int(input("Enter a positive integer: "))
##        
##        infile.write(str(num) + '\n')
##

main()
