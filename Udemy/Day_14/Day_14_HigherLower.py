from HLart import logo, vs
from HLdata import data
import random
import os

B = random.sample(data, k=1)


def HL(B, count, win):
    os.system('clear')
    print(logo)
    A = B
    if (win == 1):
        print(f"You're right! Current score: {count}.")
    elif (win == -1):
        print(f"Sorry, that's a wrong answer. Your final score is : {count}.")
        return

    print(f"Compare A : {A['name']}, {A['description']}, from {A['country']}")
    B = random.sample(data, k=1)
    print(vs)
    print(f"Against B : {B['name']}, {B['description']}, from {B['country']}")

    high = input("Who has more followers? Type 'A' or 'B' : ").lower()

    if (high == "a" and A['follower_count'] > B['follower_count']):
        HL(B, count + 1, 1)
    elif (high == "b" and B['follower_count'] > A['follower_count']):
        HL(B, count + 1, 1)
    else:
        HL(B, count, -1)


print("asd")

HL(B, 0, 0)
