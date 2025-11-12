from globals import MINE, BLANK, HIDDEN
from adjust_board import adjust_board 

def update_board(base_board, player_board, row, col):
    if base_board[row][col] == MINE:
        player_board[row][col] = MINE
        return True  # a mine was hit

    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if player_board[r][c] != HIDDEN:
            break # already revealed