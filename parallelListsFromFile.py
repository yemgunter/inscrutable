
def main():
    friends_file = open("friends.txt", 'r')
    name_list = []
    age_list = []
    food_list = []

    name = friends_file.readline()
    while name != "":
        name = name.rstrip('\n')
        name_list.append(name)
        age = int(friends_file.readline())
        age_list.append(age)
        food = friends_file.readline().rstrip('\n')
        food_list.append(food)
        name = friends_file.readline()
    
    
    friends_file.close()

    display_friends(name_list, age_list, food_list)
    
def display_friends(names, ages, foods):
    print(format("Name", '20'), format("Age", '5'),
          format("Favorite food", '25'))
    for i in range(len(names)):
        print(format(names[i], '20'), format(str(ages[i]), '5'),
              format(foods[i], '25'))

main()



