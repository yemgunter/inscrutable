## Ch 7 Lists and Tuples


##Finding items in list with IN operator

# This program demonstrates the in operator

# used with a list.

##def main():
##
##    # Create a list of product numbers.
##    prod_nums = ['V475', 'F987', 'Q143', 'R688']
##
##    # Get a product number to search for.
##    search = input('Enter a product number: ')
##
##    # Determine whether the product number is in the list.
##    if search in prod_nums:
##        print(search, 'was found in the list.')
##    else:
##        print(search, 'was not found in the list.')
##
### Call the main function.
##main()


def main():
    # Create a list of grocery items.
    grocery_list = ['apples', 'peanut butter', 'eggs', 'spinach',
                    'coffee', 'avocado']

    # Search for a grocery item.
    search = input('Enter an item: ')

    # Determine whether the item is in the list.
    if search in grocery_list:
         print('The item', search, 'was found in the list.')
    else:
         print('The item', search, 'was not found in the list.')

# Call the main function.
main()
