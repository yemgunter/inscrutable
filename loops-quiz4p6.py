
## Although this program has no prompt nor does it define
## any variables for an ID, it creates an infinite loop,
## it validates the input because the id has never been defined


number = input()

while number != id:
    print("This is not your ID number.")
    number = input()

print("This is your ID number:", number)


## Program was ran and tested as correct on Quiz 4.6: Input Validation Loops
