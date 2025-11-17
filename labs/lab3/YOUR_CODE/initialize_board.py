import globals
import utils
from get_validated_input import get_validated_input
from place_random_mines import place_random_mines 
from count_adjacent_bombs import count_adjacent_bombs 

# Sets up the number of rows and columns for the board
ROWS = 7
COLS = 7


def initialize_board(ROWS = 7, COLS = 7, fill = " "):
    utils.clear_screen() 
    prompt1 = "Enter the width of the board: "
    prompt2 = "The width must be between 2 and 10 (inclusive), re-enter: "  
    low = 2
    high = 10  
    globals.COLS = get_validated_input(prompt1, prompt2, low, high)   

    prompt3 = "Enter the height of the board: "
    prompt4 = "Height must be between 2 and 10 (inclusive), re-enter: "    
    globals.ROWS = get_validated_input(prompt3, prompt4, low, high)

    prompt5 = "Enter the number of random mines: "
    low = 1
    high = globals.ROWS * globals.COLS - 1
    prompt6 = f"Mines must be between 1 and {high} (inclusive), re-enter: "    
    globals.MINES = get_validated_input(prompt5, prompt6, low, high)   

    board = []    # creates an empty board
    for idx in range(globals.ROWS):
        row = []                      # creates an empty row
        for idy in range(globals.COLS):
            col = (" \u2666" , '   ')  # for each col in row create a tuple
            row.append(col)            # append tuple to row
    
        board.append(row)              # apends row to board
        board = place_random_mines(board)  # places random mines on board
        board = count_adjacent_bombs(board) # place the number of adjacent bombs for each cell 
   
    return board