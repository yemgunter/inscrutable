total_seconds = int(input("Enter number of seconds: "))

minutes = total_seconds // 60

seconds = total_seconds % 60
seconds = total_seconds - (minutes * 60)


print('\n',total_seconds, " total seconds breaks down into:", sep=''), 
print("\tminutes: ", minutes)
print("\tseconds: ", seconds)




