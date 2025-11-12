import globals

import mines 

'''
Checks to see where the bombs are located on the board
'''

def is_bomb_at():
    if 0 <= rows < len(board) and 0 <= cols < len(board[0]):
        return board[rows][cols] == MINE
    return False
