num_bagels = float(input('How many bagels would you like to order? '))

if num_bagels <= 12:
    price = num_bagels * 1.5
else:
    price = (12 * 1.5) + ((num_bagels - 12) * .75)

print('Your total is $', format(price, ',.2f'), sep='')


#

if age >= 65: 
    senior_citizens += 1
else:
    non_seniors += 1
