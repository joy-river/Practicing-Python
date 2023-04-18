from turtle import Turtle, Screen
from Snake import Snake

square_size = 2
game_on = True
snake = Snake(square_size)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_on:
    screen.update()
    snake.snake_move()


screen.exitonclick()
