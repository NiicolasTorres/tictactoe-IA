ALL_SPACES=['1','2','3','4','5','6','7','8','9']
X, O, BLANK = 'X','O',' '

def get_blank_board():
    board = {}
    
    for space in  ALL_SPACES:
        print('The space is:', space)
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


def play_tic_tac_toe():
    print('Welcome to Tic Tac Toe!')
    gameBoard = get_blank_board()

    while True:  #main game loop
        print(display_board(gameBoard))
    
        entry = None
        while not is_entry_valid(gameBoard, entry): #keep asking for the entry while not valid
            entry = input('Please enter the position you\'d like to pleace X or O: ')
    
    
    
    
play_tic_tac_toe()