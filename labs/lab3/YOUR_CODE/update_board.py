from globals import MINE, BLANK, HIDDEN
from get_adjacent_cell import get_adjacent_cells

def update_board(base_board, player_board, row, col):
    if base_board[row][col] == "+":
        player_board[row][col] = "+"  # reveal the mine
        return True  # a mine was hit

    stack = [(row, col)]
    while stack: 
        r, c = stack.pop()
        if player_board[r][c] != "#":  # only update if not already revealed
            break # already revealed