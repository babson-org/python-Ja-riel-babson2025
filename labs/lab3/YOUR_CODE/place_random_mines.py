import random
import globals  

def place_mines(board, num_mines):
    ROWS = len(board)
    COLS = len(board[0])
    placed = 0

    while placed < num_mines:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        if board[r][c] != globals.MINE:
            board[r][c] = globals.MINE
            placed += 1
