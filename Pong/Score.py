from turtle import Turtle
class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(x=130, y=200)
        self.penup()
        self.score = 0
        self.write(arg=f'{self.score}', move=False, align="center", font=("arial", 90, "bold"))
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'{self.score}', move=False, align="center", font=("arial", 90, "bold"))

class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(x=-130, y=200)
        self.penup()
        self.score = 0
        self.write(arg=f'{self.score}', move=False, align="center", font=("arial", 90, "bold"))
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'{self.score}', move=False, align="center", font=("arial", 90, "bold"))




class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.teleport(x=0, y=-300)
        self.pensize(width=10)
        while self.distance(x=0,y=-300) < 600:
            self.pendown()
            self.setheading(90)
            self.forward(25)
            self.penup()
            self.setheading(90)
            self.forward(25)