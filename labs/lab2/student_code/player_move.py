    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    # TODO: Assign score['player'] to the selected cell on the board
    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8
    ask = "Select an empty cell (1-9): "
    while True:
        try:
            move = int(input(ask)) - 1
            if move < 0 or move > 8:
                ask = "Invalid choice. Please enter a number (1-9): "
                continue
            if abs(board[move]) == 10:
                ask = "That spot has been selected! Try again! (1-9): "
                continue
            
            board[move] = score['player']
            break
        
        except ValueError:
            ask = "Invalid input. Try again (1-9): "

pass
