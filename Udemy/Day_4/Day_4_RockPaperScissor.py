import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
hand = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if (hand == 0):
    print(rock)
elif (hand == 1):
    print(paper)
else:
    print(scissors)

com_hand = random.randint(0, 2)

print("Computer chose:")

if (com_hand == 0):
    print(rock)
    if (hand == 1):
        print("You Win!")
    elif (hand == 2):
        print("You lose")
elif (com_hand == 1):
    print(paper)
    if (hand == 0):
        print("You lose")
    elif (hand == 2):
        print("You Win!")
else:
    print(scissors)
    if (hand == 0):
        print("You Win!")
    elif (hand == 1):
        print("You lose")

if (hand == com_hand):
    print("Draw")
