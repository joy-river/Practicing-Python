import os
import random
from Blackjack_art import logo


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


clearConsole()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check(cards):
    c_sum = sum(cards)
    if (c_sum > 21):  # burst
        if (11 not in cards):
            return -1
        else:
            for num in cards:
                if (num == 11):
                    num = 1
                    return check(cards)
    elif (c_sum == 21):
        return 21
    else:
        return c_sum


def Counting(p_card, c_card):
    p_check = check(p_card)

    print(
        f"Your cards : {p_card}, current score: {p_check} \nComputer's first card : {c_card[0]}")

    if (p_check == 21):
        print(f"You Win! Player has BlackJack!")
        return
    hit = input("Do you want to draw a card? Type 'y' or 'n' : ")
    while (hit == "y"):
        p_card.append(random.choice(cards))
        p_check = check(p_card)
        print(
            f"Your cards : {p_card}, current score: {p_check} \nComputer's first card : {c_card[0]}")

        if (p_check > 21):
            print("You lose,")


# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
play = input(
    "\nWelcome to the Black Jack simulator! Do you want a play? Type 'y' or 'n' : ")

while (play == "y"):
    def Blackjack():
        print(logo)
        p_card = random.choices(cards, k=2)
        c_card = [random.choice(cards)]
        Counting()

    BlackJack()
