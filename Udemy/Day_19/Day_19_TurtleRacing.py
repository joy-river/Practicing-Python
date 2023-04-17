from turtle import *

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def turtle_init(i):
    temp = Turtle("turtle", colors[i])
    colors[i] =

tim = Turtle("turtle")

tim.penup()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Choose your turtle!", prompt="Which turtle will win the race? Enter a color: ")




tim.goto(-240, 0)
print(user_bet)
screen.exitonclick()