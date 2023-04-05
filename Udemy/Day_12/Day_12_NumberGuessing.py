import random
from Guess_art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

diff = input("Choose a difficulty. Type 'ez' or 'hd' : ").lower()


def NumGuess(diff):
    if (diff == "ez"):
        attemps = 10
    else:
        attemps = 5

    Ans = random.randint(1, 100)

    while attemps > 0:
        print(f"You have {attemps} attemps remainint to guess.")
        num = int(input("Make your guess : "))
        if (num > Ans):
            print("Too high.")
        elif (num < Ans):
            print("Too low.")
        else:
            print(f"You got it! The answer if {Ans}.\nGame Over")
            return
        attemps -= 1

    print("You spent all attemps. You lose!")
    return


NumGuess(diff)
