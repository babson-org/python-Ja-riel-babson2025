while True: 
    try:
        height = int(input('Enter and odd number for the diamond height: '))
        if height % 2 == 1:
            break
        else:
            print('The number must be odd! Please try again: ')
    except ValueError:
        print('Invalid value! Please try again!')

## DEFINES THE MIDDLE OF DIAMOND PARAMETERS FOR THE WIDTH OF THE DIAMOND
middle = height // 2

## OUTLINES SPACES FOR THE LENGTH OF THE STARS FOR BOTH SPACES 
### BEFORE AND BETWEEN THE STARTING POINT OF THE DIAMOND
for idx in range (middle, -1, -1):
    before = " " * idx
    between = " " * ((middle - idx) * 2 - 1)
    if between == '':
        print(before + "*")
else:
    print(before + "*" + between + "*")

#### DEFINES THE BOTTOM HALf OF THE DIAMOND
for idx in range (1, middle + 1):
    before = " " * idx
    between = " " * ((middle - idx) * 2 - 1)
    if between == '':
        print(before + "*")
else:
    print(before + "*" + between + "*") 

