import random
#Print GAme of X and O
#Step 1
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
#test_board= ['','X','X','O','X','X','X','O','O','X']
#display_board(test_board)

#Step 2
#Function that take player input
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
    #Assign a player
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

#pc= player_input()
#player1_marker, player2_marker = player_input()
#print(player2_marker)

#Step 3
#Write a function that takes in the board list object
def place_marker(board, marker, position):
    board[position] = marker

#pm = place_marker(test_board, '$', 8)
#display_board(test_board)

#Step 4
#Check if the marker has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark or  #across
             board[4] == mark and board[5] == mark and board[6] == mark or  #across
             board[1] == mark and board[2] == mark and board[3] == mark or  #across
             board[7] == mark and board[4] == mark and board[1] == mark or  #downwards
             board[8] == mark and board[5] == mark and board[2] == mark or  #downwards
             board[9] == mark and board[6] == mark and board[3] == mark or  #downwards
             board[7] == mark and board[5] == mark and board[3] == mark or  # across
             board[7] == mark and board[8] == mark and board[9] == mark or  # across
             board[9] == mark and board[5] == mark and board[1] == mark))

#display_board(test_board)
#chw = win_check(test_board, 'X')
#print(chw)

#Step 5
#Write a function that randomly choose a player that goes first
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#Step 6
# Write a function that return boolean when a spot/position is available
def space_check(board,position):
    return board[position] == ' '

#Step 7
# Write a function that returns a boolean when the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#Step 8
#Write a function that ask a player's next position as a number 1-9 Using step 6 to see
#free position
def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position between 1-9: '))
    return position

#Step 9
#Write a function that ask a player if they want to play again
def play_again():
    choice = input('Play again? Enter Yes or No')
    return choice == 'Yes'

#Step 10
#Putting all the codes & functions together

print('=======WELCOME TO TICK-TOCK GAME')

strt_game = True

while strt_game:
    #Play the game, Set the board, who's first choose x or o
    the_board = ['']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' You go first!!')
    play_game = input('Ready to Play: Y or N: ')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    #Game on
    while game_on:
       if turn == 'Player 1':
           display_board(the_board)
            #choose position
           position = player_choice(the_board)
           place_marker(the_board,player1_marker,position)

           if win_check(the_board, player1_marker):
               display_board(the_board)
               print('PLAYER 1 HAS WON!!!')
               game_on = False
           else:
               if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a TIE!!')
               else:
                   turn = 'Player 2'
       else:
           display_board(the_board)
           position = player_choice(the_board)
           place_marker(the_board, player2_marker, position)
           if win_check(the_board, player2_marker):
               display_board(the_board)
               print('PLAYER 2 HAS WON!!!')
               game_on = False
           else:
               if full_board_check(the_board):
                   display_board(the_board)
                   print('THAT IS A TIE')
                   game_on = False
               else:
                   turn = 'Player 1'

#if not play_again():
    #break



