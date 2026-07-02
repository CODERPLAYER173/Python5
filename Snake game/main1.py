import time
from scoreboard import ScoreBoard
from SNAKE import Snake
from  food import Food
from turtle import Screen
s = Screen()
s.setup(600,600)
s.bgcolor("chartreuse1")

game = True
s.tracer(0)

snake = Snake()
food  = Food()
score = ScoreBoard()
def check():
    s.listen()
    s.onkey(snake.move_left, "w")
    s.onkey(snake.move_back, "a")
    s.onkey(snake.move_right, "s")
    s.onkey(snake.move_forward, "d")


check()
while game:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.ate()
        snake.extend()
        score.reset_high()
        score.update_score()




    if snake.head.xcor() < -295 or  snake.head.xcor() > 295 or  snake.head.ycor() < -295 or  snake.head.ycor() > 295:
        game = False
        score.game_over()

for segment in snake.turtles[:1]:
    if snake.head.distance(segment) < 15:
        game = False
        score.game_over()
s.exitonclick()
