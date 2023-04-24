from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.l_score = 0
        self.r_score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", False, "center", ('Arial', 15, 'normal'))

    def r_getscore(self):
        self.r_score += 1
        self.print_score()

    def l_getscore(self):
        self.l_score += 1
        self.print_score()
