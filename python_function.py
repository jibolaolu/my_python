from random import shuffle

example = [1, 3, 4,7,12,76, 45]
shuflist = ['', 'O', '']
shuffle(example)
print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

shuff = shuffle_list(example)
print(shuff)

lst = shuffle_list(shuflist)
print(lst)

def player_guess():
    guess = ''
    while guess not in ['0', '2', '4', '3']:
        guess = input("Pick a number: 0,2,4 and 3: ")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print('Wrong answers')
        print(mylist)

#Initial list
mylist = ['', 'O', '']

#shuffled list
mixed_list = shuffle_list(mylist)

#Guess Player
guess = player_guess()

#Check guess
check_guess(mixed_list, guess)



