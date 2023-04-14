import turtle
from turtle import *
import random as r

timmy = Turtle()

turtle.colormode(255)


def timmy_color():
    rgb = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    return rgb



def timmy_spirograph(gap):
    for i in range(int(360 / gap)):
        timmy.color(timmy_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


timmy.speed(0)
degree_sum = 0


timmy_spirograph(5)
Screen().exitonclick()
