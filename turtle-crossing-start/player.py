from turtle import Turtle as Tu


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Tu):
    def __init__(self):
         super().__init__()
         self.penup()
         self.goto(STARTING_POSITION)
         self.shape("turtle")
         self.setheading(90)
         self.shapesize(stretch_len=1 , stretch_wid=1)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def eeturn(self):
        self.teleport(0,-280)