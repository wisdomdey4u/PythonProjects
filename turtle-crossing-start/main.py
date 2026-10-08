import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

loop_counter = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    loop_counter += 1

    if loop_counter % 6 == 0:
        car_manager.create_car()

    car_manager.move_car()

    for car in car_manager.cars:
        if  player.distance(car) < 30 and abs(player.ycor() - car.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

car_manager.cars = [
    car for car in car_manager.cars if car.xcor() > -320
]

screen.exitonclick()