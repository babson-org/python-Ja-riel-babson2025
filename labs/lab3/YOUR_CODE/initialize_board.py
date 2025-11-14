import globals 


def initialize_board(rows = 7, cols = 7, fill = " "):
    """Create a board with random mines and neighbor counts."""
    return[[fill for idx in range(rows)] for idy in range(cols)]

# The board that contains all of the mines and numbers
from mines import place_miness

base_board = initialize_board(rows = 7, cols = 7)
place_mines(base_board, num_mines = 4)
print(base_board)

# The board the player uses and sees
player_board = initialize_board(rows = 7, cols = 7, fill = "*")
