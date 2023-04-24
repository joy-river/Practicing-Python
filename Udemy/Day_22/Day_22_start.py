from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("This is Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()
r_paddle.make_paddle((350, 0))
l_paddle.make_paddle((-350, 0))

game_on = True

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
ball = Ball()
score = Scoreboard()

while game_on:

    screen.update()
    ball.ball_move()

    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.y_moment *= -1

    elif ball.xcor() >= 330 or ball.xcor() <= -330:
        if ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50:
            ball.x_moment *= -1
            ball.sleeptime /= 1.5
        elif ball.xcor() >= 350:
            score.l_getscore()
            ball.x_moment = -10
            ball.goto(0, 0)
            ball.sleeptime = 0.1
        elif ball.xcor() <= -350:
            score.r_getscore()
            ball.x_moment = 10
            ball.goto(0, 0)
            ball.sleeptime = 0.1



screen.exitonclick()
