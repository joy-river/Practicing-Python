# import colorgram
import turtle
import random

timmy = turtle.Turtle()

timmy.speed(0)
timmy.pensize(10)
turtle.colormode(255)
timmy.hideturtle()
timmy.penup()
timmy.goto(-200, -200)
# colors = colorgram.extract('image.jpg', 30)
# rgb_list = []
#
# for i in colors:
#     rgb_list.append((i.rgb.r, i.rgb.g, i.rgb.b))
#
# print(rgb_list)

rgb_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
            (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
            (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
            (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def Hirst():
    for j in range(10):
        timmy.color(random.choice(rgb_list))
        timmy.dot(20)
        if j < 9:
            timmy.forward(50)

    if timmy.heading() == 0:
        pointing = 1
    else:
        pointing = -1

    timmy.left(pointing * 90)
    timmy.forward(50)
    timmy.left(pointing * 90)


screen = turtle.Screen()
screen.screensize(480, 320)

for i in range(10):
    Hirst()

screen.exitonclick()
