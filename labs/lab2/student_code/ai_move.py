def ai_move(board: list[int]):
    
    for idx in board:
        if abs(idx) != 10 : return idx

