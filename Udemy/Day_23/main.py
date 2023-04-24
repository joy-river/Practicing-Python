import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
screen.listen()

screen.onkeypress(player.move, "Up")
cars = []

game_is_on = True
make_car = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if make_car == 6:
        cars.append(CarManager())
        make_car = 0

    for car in cars:
        car.car_move(score.level)
        if car.distance(player) < 20:
            game_is_on = False
            score.over()
        if car.xcor() <= -340:
            car.hideturtle()
            cars.remove(car)

    if player.win():
        score.get_score()

    make_car += 1


screen.exitonclick()