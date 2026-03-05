from turtle import Turtle as Tu
import random
colors = ("orange", "red", "yellow", "green", "blue", "purple","orange", "red", "yellow", "green", "blue", "purple","orange", "red", "yellow", "green", "blue", "purple","orange", "red", "yellow", "green", "blue", "purple")

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_turtles = []
        self.make()
        self.car_speed = STARTING_MOVE_DISTANCE
    def make(self):
        for x in range(0,6):
            start_position = random.randint(-280, 280)
            tim = Tu("square")
            tim.color(colors[x])
            tim.penup()
            tim.shapesize(1,2)
            tim.goto(x = 280,y = start_position)
            tim.setheading(180)
            self.all_turtles.append(tim)

    def add(self):
        for x in range(0,1):
            start_position = random.randint(-280, 280)
            tim = Tu("square")
            tim.color(random.choice(colors))
            tim.penup()
            tim.shapesize(1,2)
            tim.goto(x = 280,y = start_position)
            tim.setheading(180)
            self.all_turtles.append(tim)
    def move(self):
        for x in self.all_turtles:
           x.forward(self.car_speed)
    def lol(self):
        self.car_speed += MOVE_INCREMENT