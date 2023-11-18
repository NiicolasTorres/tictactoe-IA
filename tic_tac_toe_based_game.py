import random

MARKERS = ('X', 'O', ' ')
X, O, BLANK = MARKERS

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
AI_COUNT = 0

def random_ai_move(board):
    available_spaces = [space for space in board if board[space] == BLANK]
    return random.choice(available_spaces) if available_spaces else None
    
    
def strategic_ai_move(board, player):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            board[space] = player
            if complex_check_winner(board, player, space):
                return space
            board[space] = BLANK

    opponent = O if player == X else X
    for space in ALL_SPACES:
        if board[space] == BLANK:
            board[space] = opponent
            if complex_check_winner(board, opponent, space):
                return space
            board[space] = BLANK

    strategic_moves = ['5', '1', '3', '9', '7', '4', '8', '6', '2']
    for move in strategic_moves:
        if board[move] == BLANK:
            return move

def minimax(board, depth, isMaximizing, player):
    opponent = O if player == X else X
    global AI_COUNT
    AI_COUNT += 1

    if check_winner(board, player):
        return 1
    elif check_winner(board, opponent):
        return -1
    elif check_board_full(board):
        return 0

    available_spaces = [space for space in ALL_SPACES if board[space] == BLANK]

    if isMaximizing:
        best_score = -float('inf')
        for space in available_spaces:
            board[space] = player
            score = minimax(board, depth + 1, False, player)
            board[space] = BLANK
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for space in available_spaces:
            board[space] = opponent
            score = minimax(board, depth + 1, True, player)
            board[space] = BLANK
            best_score = min(score, best_score)
        return best_score


def best_move_ai(board, player):
    best_score = -float('inf')
    best_move = None

    available_spaces = [space for space in ALL_SPACES if board[space] == BLANK]

    for space in available_spaces:
        board[space] = player
        score = minimax(board, 0, False, player)
        board[space] = BLANK

        if score > best_score:
            best_score, best_move = score, space

    return best_move



def get_blank_board():
    board = {space: BLANK for space in ALL_SPACES}
    return board

def display_board(board):
    return f'''
  {board['1']} | {board['2']} | {board['3']}   | 1 | 2 | 3
 ---|---|---  |
  {board['4']} | {board['5']} | {board['6']}   | 4 | 5 | 6
 ---|---|---  |
  {board['7']} | {board['8']} | {board['9']}   | 7 | 8 | 9
'''

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
    

def play_tic_tac_toe():
    print('Bienvenido a Tic Tac Toe!')
    gameBoard = get_blank_board()
    
    choice = ''
    while choice.lower() != 'x' and choice.lower() != 'o':
        choice = input('¿Quieres jugar como X u O?')
        if choice.lower() == 'x':
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
            entry = best_move_ai(gameBoard, current_player)
            if entry:
                print(f'IA{current_player} eligio el lugar {entry}')
                mark_board(gameBoard, entry, current_player)
        
        if complex_check_winner(gameBoard, current_player, entry):
            print(display_board(gameBoard))
            print(current_player + ' ganaste el juego')
            print(AI_COUNT)           
            break
            
        elif check_board_full(gameBoard):
            print(display_board(gameBoard))
            print('es un empate, vuelve a comenzar otro juego')
            break
        
            
        current_player, next_plyer = next_plyer, current_player
    
