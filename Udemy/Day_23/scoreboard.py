FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.level = 1
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Level = {self.level}", False, "center", FONT)

    def get_score(self):
        self.level += 1
        self.score_write()

    def over(self):
        self.reset()
        self.write("Game Over", False, "center", FONT)