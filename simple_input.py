game_lst = ['0','1','2','3']
def display_game(game_lst):
    print('Here is the current game list')
    print(game_lst)

#game_list(lst)

def position_choice():
    #lst = ['0', '1', '2']
    choice = 'wrong'
    while choice not in game_lst:
        choice = input("Pick a position (0-3): ")
        if choice not in game_lst:
            print("Sorry that is an invalid position")
    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Keep playing ? (Y or N): ")
        if choice not in ['Y','N']:
            print("Sorry I don't understand please choose Y or N")
    if choice == "Y":
        return True
    else:
        return False


#replc = replacement_choice(game_lst,2)
#print(replc)
#print(gc)

#gc=gameon_choice()
#print(gc)

game_on = True

while game_on:
    display_game(game_lst)
    position = position_choice()
    game_lst = replacement_choice(game_lst, position)
    display_game(game_lst)
    game_on = gameon_choice()

