from turtle import Turtle

pos = ((0,0), (20,0), (40,0))
class Snake:
    def __init__(self):
        self.turtles = []
        self.make()
        self.head = self.turtles[0]
    def make(self):
        for x in pos:
            self.add(x)


    def add(self,position):
        t = Turtle(shape="square")
        t.penup()
        t.color("firebrick3")
        t.goto(position)
        self.turtles.append(t)

    def extend(self):
        self.add(self.turtles[-1].position())
    def move(self):
        for X in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[X - 1].xcor()
            y = self.turtles[X - 1].ycor()
            self.turtles[X].goto(x, y)
        self.head.forward(20)


    def move_left(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def move_back(self):
        if self.head.heading() != 0:
            self.head.setheading(90+90)

    def move_right(self):
        if self.head.heading() != 90:
            self.head.setheading(90+180)

    def move_forward(self):
        if self.head.heading() != 180:
            self.head.setheading(0)