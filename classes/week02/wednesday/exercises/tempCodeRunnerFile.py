# enter code here
secret_num = 10
guess = None
while guess != secret_num:
    guess = int(input("Guess the secret number: "))
    if guess != secret_num:
        print("Wrong answer, guess again!")
print("Correct! You guessed the secret number!")

pause=input('pause')