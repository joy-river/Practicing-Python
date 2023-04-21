from turtle import Turtle


class Paddle (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.width = 20
        self.height = 100

    def make_paddle(self, pos):
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.setpos(pos[0], pos[1])

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.forward(-20)
