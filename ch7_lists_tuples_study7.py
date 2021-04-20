## Ch 7 Lists and Tuples  7.7 barista_pay.py

# This progam calculates the gross pay for
# each of Yolanda's designers.

# NUM_EMPLOYEES is used as a constant for the
# size of the list
NUM_EMPLOYEES = 6

def main():
    # Create a list to hold employee hours
    hours = [0] * NUM_EMPLOYEES

    # Get each employees's hours worked.
    for index in range(NUM_EMPLOYEES):
        print('Enter the hours worked by employee ',
              index + 1, ': ', sep='', end='')
        hours[index] = float(input())

        # Get the hourly pay rate.
        pay_rate = float(input('Enter the hourly pay rate: '))

        # Display each employee's gross pay.
        for index in range(NUM_EMPLOYEES):
            gross_pay = hours[index] * pay_rate
            print('Gross pay for employee ', index + 1, ': $',
                  format(gross_pay, ',.2f'), sep='')

# Call the main function.
main()
        


