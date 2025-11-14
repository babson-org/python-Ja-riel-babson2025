import globals
import utils
from initialize_board import initialize_board
from print_board import print_board
from update_board import update_board
from get_validated_input import get_validated_input
from game_over import game_over
from is_bomb_at import is_bomb_at
from mines import place_mines
from initialize_board import base_board


def play_minesweep():
    print("Welcome to Minesweeper!")
    rows = int(input("Enter number a number between 1 - 7 for your rows: "))
    cols = int(input("Enter number a number between 1 - 7 for your columns: "))
    num_mines = int(input(f"Enter number of mines (1 - {rows * cols - 1}): "))

    base = initialize_board(rows, cols)
    place_mines(base_board, num_mines)
    player_board = initialize_board(rows, cols, fill = "+")

    while True:
        print_board(player_board)
        r, c = get_validated_input(rows, cols)

        if is_bomb_at(base_board, r, c):
            print("Boom! You hit a mine. Game Over!")
            game_over(base_board, player_board)
            break
        else:
            update_board(base_board, player_board, r, c)
            if utils.check_win(player_board, base_board, num_mines):
                print("Congratulations! You've cleared the board!")
                game_over(base_board, player_board)
                break

    play_minesweep()
