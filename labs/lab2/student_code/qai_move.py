def ai_move(board: list[int]):
    """
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
    # TODO: Loop through board
        # CREATE THE BOARD
        # IDENTIFY THE USER AND THE ASK THEM TO PICK A NUMBER FOR 'X' OR 'O'
        # CODE THE DEFAULT NUMBER THAT THE COMPUTER WILL USE TO BE 'X' OR '0'
        # CREATE A FOR LOOP 
        # THAT ALLOWS THE COMPUTER TO ANTICIPATE THE NEXT MOVE OF THE USER
    # TODO: Find the first index where abs(cell) != 10
        # CREATE A FOR LOOP (OR WHILE LOOP) TO DETERMINE WHERE THE COMPUTER WILL PLACE
        # ITS 'X' OR 'O' AFTER THE USER'S INPUT
    # TODO: Return that index as the AI's move
        # PRINT THE OUT PUT OF WHERE THE COMPUTER ITS MOVE
    pass