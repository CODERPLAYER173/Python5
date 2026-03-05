import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
cars = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
player  = Player()
game_is_on = True
screen.listen()
screen.onkeyrelease(player.move,"w")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    random_number = random.randint(0, 100)
    if random_number % 5 == 0:
        cars.add()
    if player.ycor() == 280:
        score.update_score()
        player.eeturn()
        cars.lol()
    if score.level == 5:
        score.game_win()
        game_is_on = False
    for x in cars.all_turtles:
        if player.distance(x) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()