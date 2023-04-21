from turtle import Turtle
import time


class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.setpos(0, 0)
        self.x_moment = 10
        self.y_moment = 10

    def ball_move(self):
        self.setx(self.xcor() + self.x_moment)
        self.sety(self.ycor() + self.y_moment)
        time.sleep(0.05)


