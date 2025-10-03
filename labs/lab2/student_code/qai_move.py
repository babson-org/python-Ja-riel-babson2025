import sys

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
board = [str(i) for i in range(1,10)]
def create_board(board: list [int | str]):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    # IDENTIFY THE USER AND THE ASK THEM TO PICK A NUMBER FOR 'X' OR 'O'
'X' == 10
'O' == -10
score = {'player': 10, 'ai': -10}
    # CODE THE DEFAULT NUMBER THAT THE COMPUTER WILL USE TO BE 'X' OR '0'
Game_symbols = []

for cell in board:
    if cell == 10:
        Game_symbols.append("X")
    elif cell == -10:
        Game_symbols.append("O")
    else:
        Game_symbols.append(str(cell))
    # THAT ALLOWS THE COMPUTER TO ANTICIPATE THE NEXT MOVE OF THE USER

   # TODO: Find the first index where abs(cell) != 10
        # CREATE A FOR LOOP (OR WHILE LOOP) TO DETERMINE WHERE THE COMPUTER WILL PLACE
        # ITS 'X' OR 'O' AFTER THE USER'S INPUT
    # TODO: Return that index as the AI's move
        # PRINT THE OUT PUT OF WHERE THE COMPUTER ITS MOVE
def available_moves(board: list[int]): list[int]:
    """
    Returns list of indices where moves are still possible.
    """
    for idx in idx, cell in enumerate(board):
        if abs(cell) != 10: 
    return None

def play_game():
    """
    Runs a full game of Tic-Tac-Toe between the player and the AI.
    """
    # TODO: Find the first index where abs(cell) != 10
        # CREATE A FOR LOOP (OR WHILE LOOP) TO DETERMINE WHERE THE COMPUTER WILL PLACE
        # ITS 'X' OR 'O' AFTER THE USER'S INPUT
 # Get player name and assign AI name.
    ai_name = 'Big Mean Machine'
    player_name = input('Please enter your name: ')

    # First Player uses +10, Second Player uses -10.
    score = {'player_name': 10, 'ai_name': -10}  # defualt human goes first

    # Tracks whose turn it is. True = player's turn, False = AI's turn.
    
    # Initialize an empty board: numbers 1-9 represent available spaces.
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # The "player_win" variable stores the winning score used for comparisons later.
    # By default, 30 means the player wins.
    player_win = 30

    # Set difficulty: False = easy (random AI), True = hard (minimax AI).
    play_hard = False  # TODO: Change to False once ai_move.py is ready.

    # Clear the screen to start fresh.
    clear_screen()

    
    sys.stdout.flush()

    # Ask who plays first: 1 = player, 2 = computer.
    txt = 'Who plays first (1/you, 2/computer)? '
    while True:
        try:
            first_to_play = int(input(txt))
            # Input must be 1 or 2 only.
            if first_to_play not in (1, 2):
                raise ValueError
            break
        except ValueError:
            # If invalid input, ask again.
            txt = 'Please enter 1 or 2 '

    # If the AI plays first, swap scoring roles and set playerTurn to False.
    if first_to_play == 2:
        score['player'], score['ai'] = score['ai'], score['player']
        playerTurn = False
        player_win = -30  # Winning score reversed if AI goes first.

    # Main game loop: continues until game_over(board) returns True.
    while not game_over(board):
        # Show the current board.
        print_board(board)

        if playerTurn:
            # Player's turn: prompt for move.
            print(f"{player_name} moves")
            player_move(board, score)
        else:
            # AI's turn.
            print(f"{ai_name} moves")
            time.sleep(2)  # Add delay for dramatic effect.

            # Choose AI move: hard mode uses minimax, easy mode uses random.
            if play_hard:
                move = find_move(board, playerTurn)
            else:
                move = ai_move(board)

            # Mark AI's move on the board.
            board[move] = score['ai']

        # Switch turns.
        playerTurn = not playerTurn

    # Game over: display final board state.
    print_board(board)

    # Calculate final score.
    score = calc_score(board)

    # Display result.
    if score == player_win:
        print(f"Congratulations {player_name}, you beat me. Big Deal!\n")
    elif score == -player_win:
        print(f"I WON! I WON! The {ai_name} WON!!\n")
    else:
        print("It's a tie!\n")

    # TODO: Return that index as the AI's move
        # PRINT THE OUT PUT OF WHERE THE COMPUTER ITS MOVE

pass

