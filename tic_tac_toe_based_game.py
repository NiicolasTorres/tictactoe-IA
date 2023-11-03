import random


ALL_SPACES=['1','2','3','4','5','6','7','8','9']
X, O, BLANK = 'X','O',' '

def random_ai_move(board):
    available_spaces = []
    
    for  space in board:
        if board[space] == BLANK:
            available_spaces.append(space)
            
    if len(available_spaces) > 0 :
        return random.choice(available_spaces)
    else:
        return None

def get_blank_board():
    board = {}
    
    for space in  ALL_SPACES:
        print('El espacio:', space)
        board[space] = BLANK
        
    return board

def display_board(board):
    return'''
  {} | {} | {}   | 1 | 2 | 3
 ---|---|---  |
  {} | {} | {}   | 4 | 5 | 6
 ---|---|---  |
  {} | {} | {}   | 7 | 8 | 9
'''.format( 
           board['1'],board['2'],board['3'],
           board['4'],board['5'],board['6'],
           board['7'],board['8'],board['9'],
           )

def is_entry_valid(board, entry):
    
    return entry in ALL_SPACES and board[entry] == BLANK

def mark_board(board, entry, player_mark):   
    board[entry] = player_mark
    print(board)
    
    
def check_board_full(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True
    
    
    
    
def check_winner(board, player_mark):
    b,p = board, player_mark
    return (
        (b['1'] == b['2'] == b['3'] == p) or #accros the top
        (b['4'] == b['5'] == b['6'] == p) or #accros the middle
        (b['7'] == b['8'] == b['9'] == p) or #accros the bottom
        (b['1'] == b['4'] == b['7'] == p) or #accros the left
        (b['2'] == b['5'] == b['8'] == p) or #accros the middle      
        (b['3'] == b['6'] == b['9'] == p) or #accros the right
        (b['1'] == b['5'] == b['9'] == p) or # across the diagonal
        (b['7'] == b['5'] == b['3'] == p) # across the diagonal
            )
    
def complex_check_winner(board, player_mark, entry):
    all_winning_combos= [
        ['1','2','3'],['4','5','6'],['7','8','9'],
        ['1','4','7'],['2','5','8'],['3','6','9'],
        ['1','5','9'],['3','5','7']       
    ]
    
    for combo in all_winning_combos:
        if entry in combo and all(board[space] == player_mark for space in combo):
            return True
    return False
    
 #   for combo in all_winning_combos:
 #       if entry in combo:
 #           count = 0
 #           for space in combo:
 #               if board[space] == player_mark:
 #                   count += 1  # count = count + 1
 #           if count == 3:
 #               return True
 #  return False

def play_tic_tac_toe():
    print('Bienvenido a Tic Tac Toe!')
    gameBoard = get_blank_board()
    
    choice = ''
    while choice.lower() != 'x' and choice.lower() !='o':
        choice = input('¿Quieres jugar como X u O?')
        if choice.lower() == 'X':
            real_player, ai_player = X, O
        else:
            real_player, ai_player = O, X
    
    gameBoard = get_blank_board()
    
    current_player, next_plyer = X, O

    while True:  #main game loop
        if current_player == real_player:
            print(display_board(gameBoard))
        
            entry = None
            while not is_entry_valid(gameBoard, entry): #keep asking for the entry while not valid
                entry = input(f'Por favor, ingrese la posición en la que desea colocar a {current_player} >')
            mark_board(gameBoard, entry, current_player)
        else:
            entry = random_ai_move(gameBoard)
            if entry:
                print(f'IA{current_player} eligio el lugar {entry}')
                mark_board(gameBoard, entry, current_player)
        
        if complex_check_winner(gameBoard, current_player, entry):
            print(display_board(gameBoard))
            print(current_player + ' ganaste el juego')           
            break
            
        elif check_board_full(gameBoard):
            print(display_board(gameBoard))
            print('es un empate, vuelve a comenzar otro juego')
            break
        
            
        current_player, next_plyer = next_plyer, current_player
    
    
    
    
play_tic_tac_toe()