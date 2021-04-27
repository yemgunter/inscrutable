## Ch 8.2 Strings slicing

### Write an expression whose value is the string
### that consists of the first four characters of string s.
#s[0:4]


### Write an expression whose value is a string
### containing the first character of the value of name.
##name[0]


### Write an expression whose value is the string
### consisting of all the characters (starting with the sixth) of string s.
##s[5:]

##first_name = "Clovis"
##last_name = "Bagwell"
##
##full_name = first_name + ' ' + last_name
##
##print(full_name)


##first_name = input('Enter your first name: ')
##
##last_name = input('Enter your last name: ')
##
##print('Hello', first_name, last_name)
##

# nested function
##hours = int(input('How nany hours did you work? '))
##pay_rate = float(input('What is your hourly pay rate? '))
##pay = hours * pay_rate
##
##print('Your pay is' , pay)


# This program gets and item's original price and
# calculates its sale price, with a 20% discount.

# Get the item's original price
original_price = float(input("Enter the item's original price: "))

# Calculate the amunt of the discount
discount = original_price * 0.2

 #Calculate the new price with discount
sale_price = original_price - discount

# Display the item's sale price
print("The sale price is" , sale_price)


