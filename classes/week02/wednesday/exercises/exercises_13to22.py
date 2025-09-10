
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
# enter code here
num = int(input("Enter a number please: "))
if num > 0:
    print("The number entered is POSITIVE.")
elif num < 0:
    print("The number entered is NEGATIVE.")
else:
    print("The number is ZERO.")

pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
# enter code here
num = int(input("Enter a number please: "))
if num % 2 == 0:
    print("The number entered is EVEN.")
else:
    print("The number entered is ODD.")

pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
# enter code here
a = int(input("Enter first number please: "))
b = int(input("Enter second number please: "))

if a > 0 and b > 0:
    print("Both numbers entered are POSITIVE.")
elif a > 0 or b > 0:
    print("At least one number is POSITIVE.")
else:
    print("The numbers entered are NEGATIVE.")
pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
# enter code here
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
# enter code here
secret_num = 10
guess = None
while guess != secret_num:
    guess = int(input("Guess the secret number: "))
    if guess != secret_num:
        print("Wrong answer, guess again!")
print("Correct! You guessed the secret number!")

pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
# enter code here
for i in range(1, 11):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here
def square(x):
    return x * x
print("Square of 5: ", square(5))
print("Square of 10: ", square(10))

pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here
def add_item(lst, item):
    lst.append(item)

my_list = [1, 2, 3]
print("Before: ", my_list)
add_item(my_list, 4)
print("After: ", my_list)

pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here
def greet(name):
    # Capitalize the name before greeting
    name = input("Please enter your name: ")
    name = name.capitalize()
    """
    The function prints a greeting.
    By taking the user's name,
    capitalizing it, then
    including it in the message.
    """
    print(f"Hello, {name}!")
greet(" ")

pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here
names = []
for i in range(5):
    name = input(f"Enter name please {i+1}: ")
    names.append(name.capitalize())
names.sort()
print("Sorted names: ", names)

pause=input('pause')
clear_screen()

