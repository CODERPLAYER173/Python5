import time
from turtle import Screen
from paddle import Paddle1,Paddle2
from Ball import Ball
from  Score import Score1,Boundary,Score2

game_on = True
screen = Screen()


screen.setup(800,600)
screen.tracer(0)
screen.bgcolor("black")
user_paddle1 = Paddle1()
user_paddle2 = Paddle2()
ball = Ball()
score1 = Score1()
score2 = Score2()


boundary = Boundary()
screen.listen()
screen.onkeyrelease(user_paddle1.up,"w")
screen.onkeyrelease(user_paddle1.down,"s")
screen.onkeyrelease(user_paddle2.up,"Up")
screen.onkeyrelease(user_paddle2.down,"Down")
while game_on:
    score = score1.score + score2.score
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif ball.distance(user_paddle1) < 30 or ball.distance(user_paddle2) < 30:
        ball.bounce_from_paddle()
    elif ball.xcor() > 400:
        ball.hideturtle()
        ball.__init__()
        score2.update_score()
    elif  ball.xcor() < -410:
        ball.__init__()
        score1.update_score()
    if score > 15:
        game_on = False

