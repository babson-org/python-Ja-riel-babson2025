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
