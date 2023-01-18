import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()

player = Player()

screen.listen()
screen.onkey(player.move_turtle, "Up")

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        scoreboard.level += 1
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.speed_increment()


screen.exitonclick()
