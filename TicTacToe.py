from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    
    
    
def player_input():    
    marker = ''    
    while marker != 'X' and marker != 'O':        
        marker = input('Player 1, choose X or O: ').upper()               
    if marker == 'X':        
        return ('X', 'O')
    else:
        return('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker
    
    

    

def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[7] == board[5] == board[3] == mark)
    
    

import random
def choose_first():
    return 'Player {}'.format(random.randint(1,2))



def space_check(board, position):
    return board[position] == ' '



def full_board_check(board):
    for x in range(1,10):
        if space_check(board, x):
            return False
    return True
        
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Please enter a number: '))
    return position
def replay():
    restart = input('Restart? Y or N: ').lower()
    return restart == 'y' 
# Game
while True:    
    TTBoard = [' '] * 10
    (p1_marker, p2_marker) = player_input()
    chance = choose_first()
    print(chance + ' will start the game.')
    
    ready = input('Ready to play? Enter Y or N: ')
    
    if ready.lower() == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if chance == 'Player 1':
            display_board(TTBoard)
            position = player_choice(TTBoard)
            place_marker(TTBoard, p1_marker, position)      
            
            if win_check(TTBoard, p1_marker):
                display_board(TTBoard)
                print ('Player 1 has won!!')
                game_on = False
            elif full_board_check(TTBoard):
                display_board(TTBoard)
                print('The game is draw!!')
                break
            else:
                chance = 'Player 2'
                
        else:
            display_board(TTBoard)
            position = player_choice(TTBoard)
            place_marker(TTBoard, p2_marker, position)
            
            if win_check(TTBoard, p2_marker):
                display_board(TTBoard)
                print ('Player 2 has won!!')
                game_on = False
            elif full_board_check(TTBoard):
                display_board(TTBoard)
                print('The game is draw!!')
                break
            else:
                chance = 'Player 1'
            
    if not replay():
        break