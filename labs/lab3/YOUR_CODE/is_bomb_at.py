import globals

import mines 

'''
Checks to see where the bombs are located on the board
'''

def is_bomb_at():
    if 0 <= ROWS < len(board) and 0 <= COLS < len(board[0]):
        return board[ROWS][COLS] == "+"
    return False
