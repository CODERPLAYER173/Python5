from turtle import Turtle as Tu

class Paddle1(Tu):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.speed("fastest")
        self.teleport(x=-350,y=0)

    def up(self):
        self.forward(50)

    def down(self):
        self.backward(50)

class Paddle2(Tu):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=0.50)
        self.speed("fastest")
        self.teleport(x=350,y=0)

    def up(self):
        self.forward(50)

    def down(self):
        self.backward(50)