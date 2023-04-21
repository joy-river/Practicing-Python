from turtle import Turtle
import time


class Snake:
    def __init__(self, square_size):
        self.snake = []
        self.square_size = square_size

        head = Turtle("square")
        head.shapesize(square_size, square_size)
        head.color("white")
        head.penup()
        self.snake.append(head)

        for i in range(2):
            self.make_snake()

    def make_snake(self):
        temp = Turtle("square")
        temp.shapesize(self.square_size, self.square_size)
        temp.color("white")
        temp.penup()
        tail = self.snake[len(self.snake) - 1]

        xcor = tail.xcor()
        ycor = tail.ycor()

        if tail.heading() % 180 == 0:
            xcor += int((tail.heading() - 90) / 90) * 20 * self.square_size
        else:
            ycor += int((tail.heading() - 180) / 90) * 20 * self.square_size

        temp.setpos(xcor, ycor)
        self.snake.append(temp)

    def snake_move(self):
        time.sleep(0.1)
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setpos(self.snake[i - 1].pos())
        self.snake[0].forward(20 * self.square_size)


    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
