# Chapter 2.8 More about Data Output

# Suppress print functions ending newline

print('One')
print('Two')
print('Three')

print()

#On same line
print('One', end=' ')
print('Two', end=' ')
print('Three')
print()

##
###Same line no spaces tho
##print('One', end='')
##print('Two', end='')
##print('Three')
##print()
##
##
###Same as above -- same line no spaces using sep='' item separator
##print('One', 'Two', 'Three', sep='')
##print()
##
##
###Same as above -- same line BUT using sep='*' item separator
##print('One', 'Two', 'Three', sep='*')
##print()
##
##print('One', 'Two', 'Three', sep='~~~')
##print()





##total_seconds = int(input("Enter number of seconds: "))
##
##minutes = total_seconds // 60
##
##seconds = total_seconds % 60
##seconds = total_seconds - (minutes * 60)
##
##
##print('\n',total_seconds, " total seconds breaks down into:", sep=''), 
##print("\tminutes: ", minutes)
##print("\tseconds: ", seconds)
##
##
##
##temperature = float(input('What is the temperature? '))

##
##num_1 = int(input('Enter the value of num_1: '))
##num_2 = int(input('Enter the value of num_2: '))
##print(num_1 + num_2)
##
##
print(format(12345.6789, ',.2f' ))


exchange_rate = 1 / 7
print('Rate is $', format(exchange_rate, '.3f'), sep='')



