## Ch 8.1 Strings for loop accessing individual characters in a string


## Write an expression whose value is the character at index 3 of string s.
#s[3]

## Write an expression whose value is the last character in string s.
#s[-1]



##name = 'Juliet'
##for ch in name:
##    print(ch)

##name = 'Juliet'
##for ch in name:
##    ch = 'X'
##    print(name)

##my_string = 'Roses are red'
##ch = my_string[6]
##print(ch)
##print(my_string[0], my_string[6], my_string[10])


##city = 'Boston'
##print(city[6])

##city = 'Boston'
##index = 0
##while index < 6:
##    print(city[index])
##    index += 1


##city = 'Boston'
##size = len(city)
##print(size)


# Concatenate Strings

# Write an expression that is the concatenation of the
# strings "Hello" and "World".
##'Hello' + 'World'


## Write an expression that is the concatenation of two strings s1 and s2.
#s1 + s2


## Write an expression whose value is the
## concatenation of the three strigs
## name1, name2, and name3, separated by commas.
## So if name1, name2, and name3, were (respectively)
## "Neville", "Dean", and "Seamus",
## your expression's value would be "Neville,Dean,Seamus".
#name1+','+name2+','+name3

def main():
    name = 'Yolanda'
    print('The name is', name)
    name = name + ' Gunter'
    print('Now the name is', name)

main()
