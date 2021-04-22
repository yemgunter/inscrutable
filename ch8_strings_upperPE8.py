def main():
   sentences = "my friend, Amon, Gus went to the park. \
     my cat is on the keyboard. he fell off the\
   swing."

   print("Before\n", sentences)
   sentences = sentences_cap(sentences)

   print("After\n", sentences)

def sentences_cap(old_string):
    new_string = old_string[0].upper()

    #for i in range(1, len(old_string)):
    index = 1
    while index < len(old_string):
        if old_string[index] == '.' and \
           index < len(old_string)-1:
            if old_string[index] == '.':
            # copy over the '.' 
                new_string += old_string[index]
            # copy over the ' '
                new_string += old_string[index+1]
            # copy over the next character capitalized
                new_string += old_string[index+2].upper()
            # advance our index 3 characters
                index += 3
        else:
            new_string += old_string[index]
            index += 1
    return new_string

main()
