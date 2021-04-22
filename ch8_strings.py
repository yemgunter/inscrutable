def main():
    #message = "Don't cheat yourself, treat yourself"
    message = "aabc"
    ch = input("Enter a character: ")
    
    count = 0
    for character in message:
        if ch in message:
            count += 1

    print(count)










main()
