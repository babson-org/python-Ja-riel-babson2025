ROWS = 7
COLS = 7


def initialize_board(ROWS = 7, COLS = 7, fill = " "):
    initialize_board = [
        [["+" for idy in range(COLS)] for idx in range(ROWS)],
        [[" " for idy in range(COLS)] for idx in range(ROWS)]
    ]

# The board that contains all of the mines and numbers
from mines import place_mines
base_board = initialize_board[0]

# The board the player uses and sees
player_board = initialize_board[1]

print(initialize_board)
