'''
List the code for game_over, while including the conditions
for the game being won
'''


from globals import MINE

def game_won(base_board, player_board):
    """Checking if the game is won."""
    for r in range(len(base_board)):
        for c in range(len(base_board[0])):
            if base_board[r][c] != MINE and player_board[r][c] == globals.HIDDEN:
                return False
        for i in range(len(base_board, row, col)):
            return base_board[row][col] == MINE  # will detect if the game is lost
        else:
            return True




