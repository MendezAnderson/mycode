#!/usr/bin/env python3
import random

def main():
    """rock, paper, scissors"""
    num = random.randint(1, 3)
    guess = 0
    rounds = 0
    victory = 0

    while rounds < 5 and guess != num:
        if guess == 1:
            ComputerGuess = "rock"
        elif guess == 2:
            ComputerGuess = "paper"
        else:
            ComputerGuess = "scissors"

        print("Rock, Paper, Scissors")
        playerGuess = input("Enter your input: ").lower()
        validchoice = False

        while not validchoice:
            if playerGuess == "rock" or playerGuess == "paper" or playerGuess == "scissors":
                print("Valid choice")
                validchoice = True
                if playerGuess == ComputerGuess:
                    print("It's a tie!")
                elif (playerGuess == 'rock' and ComputerGuess == 'scissors') or \
                     (playerGuess == 'paper' and ComputerGuess == 'rock') or \
                     (playerGuess == 'scissors' and ComputerGuess == 'paper'):
                    print("You win!")
                    victory += 1
                else:
                    print("Computer wins!")
            else:
                print("Invalid choice. Try again.")
        break

if __name__ == "__main__":
    main()

