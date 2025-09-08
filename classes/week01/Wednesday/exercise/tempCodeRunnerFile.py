for i, item in enumerate(mylist):
    shifted_list[(i + 3) % length] = item
print(shifted_list)