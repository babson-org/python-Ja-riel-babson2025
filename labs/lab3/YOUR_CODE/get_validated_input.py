def get_validated_input(ROWS, COLS):
    """Prompt until user enters valid coordinates."""
    while True:
        try:
            prompt = input("Enter row,col (e.g., 1,2): ").split
            r, c = map(int, prompt)
            if 0 <= r < ROWS and 0 <= c < COLS:
                return r, c
            else: print("Out of range. Try again!")
        except ValueError:
            print("Invalid input. Try again!")
