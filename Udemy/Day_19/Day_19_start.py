# import turtle
# from turtle import *
#
# tim = Turtle()
# screen = Screen()
# screen_dic = {
#     "w": "move_forward"
# }
#
#
# def move(key):
#     if key == "w":
#         return move_forward()
#
#
# def move_forward():
#     tim.fd(20)
#
#
# def move_backward():
#     tim.fd(-20)
#
#
# def screen_clear():
#     screen.resetscreen()
#
# def turn_right():
#     tim.right(10)
#
# def turn_left():
#     tim.left(10)
#
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_forward)  # 함수를 다른 함수의 인수르 넣을때 ()를 생략함(고차 함수)
# screen.onkeypress(key="s", fun=move_backward)
# screen.onkeypress(key="c", fun=screen_clear)
# screen.onkeypress(key="d", fun=turn_right)
# screen.onkeypress(key="a", fun=turn_left)
# screen.exitonclick()
