


grade = int(input("Enter numeric grade between 0 and 100: "))

##if grade >= 90:
##    print("A")
##elif grade >= 80:
##    print("B")
##elif grade >= 70:
##    print("C")
##elif grade >= 60:
##    print("D")
##else:
##    print("F")

    
## Let's check for an F first...

if grade < 60:
    print("F")
elif grade < 70:
    print("D")
elif grade < 80:
    print("C")
elif grade < 90:
    print("B")
else:
    print("A")
