import random

# Computer selects a random number
secret = random.randint(1, 100)

print("Guess a number between 1 and 100")

guess = 0

while guess != secret:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print("Congratulations! You guessed the correct number.")
