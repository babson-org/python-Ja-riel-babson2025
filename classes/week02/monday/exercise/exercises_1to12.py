from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
# enter your code here
def make_tea():
    steps = [
        "Boil water",
        "Place a tea bag in a cup",
        "Pour hot water into the cup",
        "Let it steep for a few minutes",
        "Remove the tea bag",
        "Add sugar or milk if desired",
        "Enjoy your tea!"

    for step in steps:
            print(step)

    make_tea()

pause = input('pause')
clear_screen()

pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here
nums = [2, 4, 6, 8, 10]
for i in range(1, 4):
    print(nums[-1] + i * 2)

pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
first = input("Enter your first name: ")
last = input("Enter your last name: ")
print(f"Hello, {first} {last}!")


pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here
import sys, platform
print("Python version:", sys.version)
print("Platform:", platform.system(), platform.release())


pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division (/):", a / b)
print("Floor division (//):", a // b)


pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

# enter your code here
sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalized:", sentence.capitalize())
print("Split into words:", sentence.split())


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here
no_parentheses = 10 + 2 * 5 / 2 - 3 ** 2
with_parentheses = (10 + 2) * 5 / (2 - 3) ** 2
print("Without parentheses:", no_parentheses)
print("With parentheses:", with_parentheses)


pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here
foods = ["Pizza", "Sushi", "Burgers"]
foods[1] = "Pasta"
print(foods)

pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here
nums = (1, 2, 3, 4)
# nums[0] = 10  # Uncommenting this will raise an error (tuples are immutable)
print(nums)


pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here
student = {"name": "Alice", "age": 20}
student["age"] = 21
favorite_numbers = [3, 7, 11]
favorite_numbers.append(15)
print(student)
print(favorite_numbers)


pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here
quote = input("Enter your favorite quote: ")
with open("quotes.txt", "w") as f:
    f.write(quote)

with open("quotes.txt", "r") as f:
    print("Your quote:", f.read())


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here
numbers = []
for i in range(5):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)


pause=input('pause')
clear_screen()