import random

lowest = 1
highest = 100

answer = random.randint(lowest, highest)

guesses = 0
is_running = True

print("welcome to python number guesssing game")

while is_running:
    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)

        if guess < lowest or guess > highest:

            print("enter a number between (1 - 100)")

        elif guess < answer:
            print("your guess is lower")
            guesses += 1

        elif guess > answer:
            print('your guess is higher')
            guesses += 1
        else:
            is_running = False

    else:
        print("invalid guess")

print(f"you have guessed right number {answer} in {guesses} no:of guesses")
