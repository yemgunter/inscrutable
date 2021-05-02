# chapter 6 reboot 5/1/21 Saturday to beat Lab 4 to death
# replay lectures from 3/25 Thursday


def main():



############### 6.2 Using Loops to Read names out of file ##########

    infile = open("names.txt", 'r')

    for line in infile:  #for every line in file - read it!
        line = line.rstrip('\n') #strip \n from each line
        print(line)  #print each line

    
    infile.close()



main()
