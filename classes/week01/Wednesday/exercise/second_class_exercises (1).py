#%%
# print 'hello' 5 times using an arithmetic operator
print('hello' * 5)

#%%
# print 'hello' 5 times using a loop
if True:
    for i in range(5):
        print('hello')
#%%
# print 'hello' 5 times on the same line using a loop
if True:
    for i in range(5):
        print('hello', end=' ')
#%%
''' using nested loops print the following:

00 01 02
10 11 12
20 21 22

'''
for i in range(3):
    for j in range(3):
        print(i * 10 + j, end=' ')
    print()
print()
#%%
# define txt and input some text from the keyboard into it
txt = input("Enter some text: ")

#%%
# print each letter in txt
for letter in txt:
    print(letter)

#%%
# assign the variable letter to the first letter in txt
letter = txt[0]

#%%
# print out all the letters in txt that are equal to the first letter
for ch in txt:
    if ch == letter:
        print(ch, end='')
'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''

#%%
'''
# suppose we had a list of n elements. create a new list that
  shifts the elements by 3

    myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
      shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

        Hints:
             1) use len(), %, enumerate
                  2) also assign shifted_list = [None] * length  (you'll need to determine 
                          the length variable)
                               3) shift inside the for loop
                                    4) print out the printed list outside the for loop
                                    '''



                                    # %%
mylist = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(mylist)
shifted_list = [None] * length
for i, item in enumerate(mylist):
    shifted_list[(i + 3) % length] = item
print(shifted_list)