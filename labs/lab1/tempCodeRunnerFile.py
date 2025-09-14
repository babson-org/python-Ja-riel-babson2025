while True: 
    try:
        height = int(input("Enter an odd number for the diamond height: "))
        if height % 2 == 1:
            break
        else:
            print("The number must be odd and positive! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# DEFINES THE MIDDLE INDEX AND SEPERATES THE TOP & BOTTOM HALVES OF THE DIAMOND
middle = height // 2

## OUTLINES SPACES FOR THE LENGTH OF THE STARS FOR BOTH SPACES 
for idx in range (middle, -1, -1):
    before = " " * idx
    between = " " * ((middle - idx) * 2 - 1)
    if (middle - idx) * 2 - 1 == -1:
        print(before + "*")
else:
    print(before + "*" + between + "*")

#### DEFINES THE BOTTOM HALf OF THE DIAMOND
for idx in range (1, middle + 1):
    before = " " * idx
    between = " " * ((middle - idx) * 2 - 1)
    if (middle - idx) * 2 - 1 == -1:
        print(before + "*")
else:
    print(before + "*" + between + "*")