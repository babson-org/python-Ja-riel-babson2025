import globals
def get_adjacent_cells(coord, new_row, new_col, ROWS, COLS):
    adj = []

    # All relative positions around the given cell, including itself
    adjustments = [(-1, -1), (-1, 0), (-1, 1),
                   ( 0, -1), ( 0, 0), ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]

    for idx, idy in adjustments:
        # Apply the offset to the original coordinate
        new_row = coord[0] + idx
        new_col = coord[1] + idy

        # Check if the new coordinate is within the bounds of the board
        if 0 <= new_row < globals.ROWS and 0 <= new_col < globals.COLS:
            adj.append((new_row, new_col))

    return adj