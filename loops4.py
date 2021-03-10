# The "for" Loop 4.4


##MAX = 5 # The maximum number
##
##total = 0.0  # Initialize the accumulator variable
##
##print("This program calculates the sum of")
##print(MAX, "numbers you will enter.")
##
##for counter in range(MAX):
##    number = int(input("Enter a numnber: "))
##    total += number
##
##    print("The total is",  total)

##total = 0
##for count in range(1, 6):
##    total = total + count
##print(total)


total = 0.0
for count in range(3): # write a for clause with the correct range
    number = float(input("Enter a nunber: "))
    total += number
print("The total is", total)
