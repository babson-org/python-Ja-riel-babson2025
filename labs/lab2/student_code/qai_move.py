def ai_move(board: list[int]):
    """
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
    
    import sys

    # TODO: Loop through boardt
        # CREATE THE BOARD
board = [str(i) for i in range(1,10)]
def create_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

    for idx in range(9):
        if abs(board[idx]) != 10: return idx 

'X' == 10
'O' == -10
score = {'player': 10, 'ai': -10}

create_board(board)
        # IDENTIFY THE USER AND THE ASK THEM TO PICK A NUMBER FOR 'X' OR 'O'
        # CODE THE DEFAULT NUMBER THAT THE COMPUTER WILL USE TO BE 'X' OR '0'
        # THAT ALLOWS THE COMPUTER TO ANTICIPATE THE NEXT MOVE OF THE USER
ai_name = 'Big Mean Machine'
player_name = input('Please enter your name: ')
sys.stdout.flush()

print(input('Please select either "X" or "O": '))



    # TODO: Find the first index where abs(cell) != 10
        # CREATE A FOR LOOP (OR WHILE LOOP) TO DETERMINE WHERE THE COMPUTER WILL PLACE
        # ITS 'X' OR 'O' AFTER THE USER'S INPUT
    # TODO: Return that index as the AI's move
        # PRINT THE OUT PUT OF WHERE THE COMPUTER ITS MOVE

pass