res = input('Kindly input a number: ')

reslt = int(res)
print(reslt)

print(type(reslt))

#Validate User input
def user_choice():
    choice = 'WRONG'
    while choice.isdigit() == False:
        choice = input("Please enter a number (0-10): ")
        if choice.isdigit() == False:
            print("You need to enter a digit")
        elif choice not in range(0,11):
            print("You have entered number above the range")
    return int(choice)

uc = user_choice()
print(uc)