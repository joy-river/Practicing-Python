from turtle import *
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def turtle_init(i):
    temp = Turtle("turtle")
    temp.color(colors[i])
    temp.penup()
    temp.goto(-240, (int(len(colors) / 2) - i) * 30)
    return temp


def turtles_forward():
    while True:
        for i in turtles:
            i.forward(randint(1, 10))
            if int(i.xcor()) >= 240:
                return i.pencolor()


screen = Screen()
screen.setup(width=500, height=400)

for i in range(len(colors)):
    turtles.append(turtle_init(i))

user_bet = screen.textinput(title="Choose your turtle!", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    winner = turtles_forward()
    if user_bet == winner:
        print(f"Your turtle has win! The winner is {winner}!")
    else:
        print(f"You lose... The winner is {winner}!")


screen.exitonclick()
