#!/usr/bin/env python3
import random

def main():
    """Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
    num = random.randint(1, 100)
    rounds = 0

    while rounds < 5:
        guess = input("Guess a number between 1 and 100:\n> ")

        if guess.isdigit():
            guess = int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds += 1

        elif guess < num:
            print("Too low!")
            rounds += 1

        else:
            print("Correct!")
            return

    print("Out of guesses! The number was", num)


# call our main function
if __name__ == "__main__":
    main()
