import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@€$#%({)}],/<\.>[*^&"

while True:
    length = int(input("What length would you like your password to be ? :   "))
    count = int(input("How many passwords would you like ?: "))
    for x in range(0, count):
        password = ""
        for x in range(0, length):
            password_characters = random.choice(characters)
            password = password + password_characters
        print("Here is your password : ", password)

    choice = input("Want some more passwords? (y/n) ? :  ")
    if choice in ['y', 'Y', 'yes', 'Yes']:
        pass
    elif choice in ['n', 'N', 'no', 'No']:
        break
    else:
        break