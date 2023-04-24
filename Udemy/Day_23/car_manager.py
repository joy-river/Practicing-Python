COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random as r


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.color(r.choice(COLORS))
        self.shapesize(stretch_len=2)
        self.penup()
        self.goto(300, r.randint(-250, 250))

    def car_move(self, level):
        self.setx(self.xcor() - (level * MOVE_INCREMENT + STARTING_MOVE_DISTANCE))
