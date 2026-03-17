from turtle import Turtle as Tu
import random
class Food(Tu):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("firebrick1")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        randx = random.randint(-280,280)
        randy = random.randint(-280, 280)
        self.goto(randx,randy)
        self.speed("fastest")
    def ate(self):
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)