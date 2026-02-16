import random

secret_number = random.randint(1, 100)
attempts = 7

print("Guess the number between 1 and 100!")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high! Try a smaller number.")
    elif guess < secret_number:
        print("Too low! Try a larger number.")
    else:
        print("Congratulations! You guessed the number.")
        break

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("You lost! The correct number was:", secret_number)