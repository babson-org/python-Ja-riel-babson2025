def get_adjacent_cells(r, c, ROWS, COLS):
    adj = []
    for idx in [-1, 0, 1]:
        for idy in [-1, 0, 1]:
            if idx == 0 and idy == 0: continue
            new_r, new_c = r + idx, c + idy
            if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                adj.append((new_r, new_c))
    return adj 