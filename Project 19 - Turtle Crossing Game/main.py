import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

win = Screen()
win.setup(width=600, height=600)
win.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.create_cars()
score = ScoreBoard()

win.listen()
win.onkeypress(player.move, "Up")

game_is_on = True
create_cars_counter = 6
while game_is_on:
    time.sleep(0.1)
    win.update()

    # check for collisions
    if car_manager.collision(player):
        game_is_on = False
        score.game_over()

    # check for player finish line
    if player.ycor() > 280:
        player.reset()
        score.update_score()
        car_manager.increase_speed()

    # create cars every 0.6 seconds
    create_cars_counter -= 1
    if not create_cars_counter:
        car_manager.create_cars()
        create_cars_counter = 6

    # move cars
    car_manager.move_cars()


win.exitonclick()
