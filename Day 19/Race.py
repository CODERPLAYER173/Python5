import random
from turtle import Turtle,Screen
is_race = False
colors = ("orange", "red", "yellow", "green", "blue", "purple")
all_turtles = []
y =(-100,-70,-40,-10,20,50)
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race enter a color from a rainbow")
if user_bet:
    is_race = True
for x in range(0,6):
    tim = Turtle("turtle")
    tim.color(colors[x])
    tim.penup()
    tim.goto(x = -240,y = y[x])
    all_turtles.append(tim)

while is_race:
    for turtles in all_turtles:
        a =  turtles.xcor()
        b = turtles.pencolor()
        if a >= 230:
            is_race = False
            if b == user_bet:
                print("you win",b,"turtle is the winner")
            else:
                print("you lose",b,"turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)
screen.exitonclick()

