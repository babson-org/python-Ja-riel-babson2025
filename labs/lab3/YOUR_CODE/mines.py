import random
import globals  

def place_mines(board, num_mines):
    rows = len(board)
    cols = len(board[0])
    landed = 0

    while placed < num_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if board[r][c] != globals.MINE:
            board[r][c] = globals.MINE
            placed += 1

def  check_cell(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] == globals.MINE
    return False