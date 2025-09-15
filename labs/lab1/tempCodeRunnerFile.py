Letters = 0
Words = 1
Sentences = 0

## ASKS THE USER TO INPUT A STRING OF TEXT
txt = input('Enter text + punctuation please: ').strip()

## COUNTS THE LETTERS, WORDS, AND SENTENCES
for char in txt:
    if char.isalpha(): 
        Letters += 1
    elif char == ' ': 
        Words += 1
    elif char in ('.', '!', '?'): 
        Sentences +=1
print(Letters)
print(Words)
print(Sentences)