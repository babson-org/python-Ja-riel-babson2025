# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()

"""
Lab 1 - Python Basics
Author: <Ja-riel Bailey>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """

    # TODO: Prompt user for an odd number
    height = int(input('Enter and odd number for the diamond height'))

    # TODO: Draw the top half of the diamond

    # TODO: Draw the bottom half of the diamond

# Uncomment to test Part 1
# draw_diamond()
## ENSURES THAT THE USER ENTERS A NUMBERIC VALUE AND NOT WORDS/INVALID VALUES
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


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")

    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0

    # TODO: Count words

    # TODO: Count sentences

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {0}")        # replace 0
    print(f"Sentences: {0}")    # replace 0

# Uncomment to test Part 2
# text_analysis()

Letters = 0
Words = 1
Sentences = 0

txt = input('Enter text + punctuation please: ').strip()
for char in txt:
    if char.isalpha(): 
        Letters += 1
    elif char == ' ': 
        Words += 1
    elif char in ('.', '!', '?'): 
        Sentences +=1
print('letters', Letters)
print('words', Words)
print('sentences', Sentences)


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """
## CREATES THE TRADITIONAL ALPHEBET TO USE FOR ENCRYPTING THE MESSAGE
text = input("Enter the message you want to encrypt: ")
alphebet = []
for idx in range(97, 97 + 26):
    alphebet.append(chr(idx))
print(alphebet)

### SHIFTS THE SEQUENCE OF THE ALPHEBET TO ENCRYPT
shift = int(input('Enter shift value: '))
if shift >= 0 or shift <= 26:
    print('Shift value must be between 1 and 26')
    exit()

shift.aLphebet = [None] * 26


for char in text: 
    if char in alphebet:
        idx = alphebet.idex(char)
        new_index = (idx + shift) % 26
        result += alphebet[new_index]
    else:
        result += char
    

print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
    result = ""

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
# caesar_cipher()

