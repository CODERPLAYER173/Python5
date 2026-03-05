import random

colors =[ (202, 164, 110), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),(240, 245, 241), (236, 239, 243), (149, 75, 50),  (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
from turtle import Turtle,Screen
import turtle
turtle.colormode(255)
t = Turtle()
t.speed(0)
screen = Screen()
y = 0
for x in range(1,101):
    t.color(random.choice(colors))
    t.begin_fill()
    t.dot(20)
    t.end_fill()
    t.penup()
    t.forward(50)
    t.pendown()
    if x % 10 == 0 :
        y += 50
        t.teleport(0,y)
screen.exitonclick()

