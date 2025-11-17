import globals
import place_random_mines 

'''
Checks to see where the bombs are located on the board
'''

def is_bomb_at():
    if 0 <= ROWS < len(board) and 0 <= COLS < len(board[0]):
        return board[ROWS][COLS] == "+"
    return False

def  check_cell(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] == '*'
    return False
