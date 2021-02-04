# if cold outside
#   wear a coat
# go to class


# if temp <= 50
#   wear a coat
# go to class

##x = 0
##y = 0
##
# if x < 0:
##    print("x is negative")
# elif x > 0:
##    print("x is positive")
# else:
##    print("x is zero")
##
# print("Bye")


# dual alternative decision structure

# if condition:
# stmt
# stmt
# ...
# elif condition:
# stmt
# ...
# stmt
# else:
# stmt
# stmt
# stmt


x = int(input("Enter an interger: "))

# if x < 0:
##    print("x is negative")
# elif x > 0:
##    print("x is positive")

# the above block is correct like the one below, just more efficient

# if x < 0:
##    print("x is negative")
# else:
# if x > 0:
##        print("x is positive")

print("Bye")
if x < 0:
    print("x is negative")
elif x > 0:
    print("x is positive")
