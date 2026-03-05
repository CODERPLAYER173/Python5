import random
from turtle import Turtle as Tu
class Ball(Tu):
    def __init__(self):
        super().__init__()
        self.ball_S = 0.5
        self.penup()
        self.shape("circle")
        self.shapesize(1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def bounce(self):
        self.y_move *= -1
    def bounce_from_paddle(self):
        self.x_move *= -1
        self.ball_S *= 0.9
