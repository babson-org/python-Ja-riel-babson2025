txt = input('Please enter some text: ')
for letter in txt:
    if letter.isalpha():
        print(letter, end = '')
print()