def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """

    """
    0 1 2
    3 4 5
    6 7 8 
    """

    if abs(board[0] + board[1] + board[2]) == 10: return board[0] + board[1] + board[2]
    elif abs(board[3] + board[4] + board[5]) == 10: return board[3] + board[4] + board[5]
    elif abs(board[6] + board[7] + board[8]) == 10: return board[6] + board[7] + board[8]
    elif abs(board[0] + board[3] + board[6]) == 10: return board[0] + board[3] + board[6]
    elif abs(board[1] + board[4] + board[7]) == 10: return board[1] + board[4] + board[7]
    elif abs(board[2] + board[5] + board[8]) == 10: return board[2] + board[5] + board[8]
    elif abs(board[0] + board[4] + board[8]) == 10: return board[0] + board[4] + board[8]
    elif abs(board[2] + board[4] + board[6]) == 10: return board[2] + board[4] + board[6]
    else: return 0