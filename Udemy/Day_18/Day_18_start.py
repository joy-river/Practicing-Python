import turtle
from turtle import *
import random as r

timmy = Turtle()
timmy.shape("turtle")

turtle.colormode(255)


def timmy_color():
    timmy.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))


def timmy_randwalk():
    timmy_color()
    timmy.right(90 * r.randint(0, 3))
    timmy.forward(50)
    timmy_randwalk()


timmy_randwalk()

Screen().exitonclick()
