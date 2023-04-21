from turtle import Turtle

font = ('Arial', 15, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score : {self.user_score}", False, "center", font)

    def over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", False, "center", font)
    def increase(self):
        self.clear()
        self.user_score += 1
        self.write(f"Score : {self.user_score}", False, "center", font)


