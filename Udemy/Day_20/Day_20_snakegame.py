from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

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

food = Food()
score = Scoreboard()
head = snake.snake[0]
while game_on:

    screen.update()
    snake.snake_move()

    if head.distance(food) < 15 * square_size:
        print("eat")
        snake.make_snake()
        score.increase()
        food.refresh()

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
         game_on = False
         score.over()

    for i in snake.snake[1:]: # slicing.. 처음 끝은 생략가능..[2 : 10 : 2][::2][::-1]
        if head.distance(i) < 15 * square_size:
            game_on = False
            score.over()

screen.exitonclick()
