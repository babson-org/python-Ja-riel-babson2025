Letters = 0
Words = 1
Sentences = 0

txt = input('Enter text please: ').strip()
for char in txt:
    if char.isalpha(): 
        Letters += 1
    elif char == '': 
        Words += 1
    elif char in ('.', '!', '?'): 
        Sentences +=1
print('letters', Letters)
print('words', Words)
print('sentences', Sentences)