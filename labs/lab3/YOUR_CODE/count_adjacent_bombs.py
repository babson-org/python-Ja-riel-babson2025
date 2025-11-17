from is_bomb_at import is_bomb_at
from get_adjacent_cell import get_adjacent_cell 
import globals

def count_adjacent_bombs(board: list ): 

    for r in range(globals.ROWS):
        for c in range(globals.COLS):
            coord = (r, c)
            if is_bomb_at(board, (r, c)): continue # if there is a bomb go back to the inner for loo

            squares = get_adjacent_cell(coord) # if it is not a bomb get list of coordinates of ajacent cells
            squares = [s for s in squares if s != (r, c)] # removes the current cell from the list   

            cnt = 0
            for  square in (squares):
                '''
                counts the number of bombs/mines in adjacent cells
                '''
                if board[square[0]][square[1]][1] == '\U0001F4A3' : cnt += 1    
            '''
            replaces the tuple at board[r][c] with tuple(diamond,cnt) or (diamond,'   ') 
            '''
            board[r][c] = (board[square[0]][square[1]][0], cnt) if cnt != 0 else (board[square[0]][square[1]][0], '   ')

    return board