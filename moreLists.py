
def main():
    int_list = []

    input_file = open("numbers.txt", 'r')

    for line in input_file:
        int_list.append(int(line))

    print(int_list)

    int_list.sort()
    int_list.reverse()

    print(int_list)

    num = int(input("Value to find: "))

    try:
        position = int_list.index(num) + 1
        print(num, "is in the list at position", position)        
    except ValueError:    
        print(num, "is not in the list")
    except Exception:
        print("An unknown error has occurred")

##    if num in int_list:
##        position = int_list.index(num) + 1  
##        print(num, "is in the list at position", position)
##    else:
##        print(num, "is not in the list")

##    if num in int_list:
##        print(num, "is in the list at position", )
##    else:
##        print(num, "is not in the list")

##    for line in input_file:
##        int_list = int_list + [int(line)]
##        print(int_list)

    input_file.close()
    
    

main()

