from turtle import Turtle,Screen
t  = Turtle()
screen = Screen()
def move_forward():
    t.forward(10)
def move_right():
    t.right(10)

def move_left():
    t.left(10)

def move_back():
    t.back(10)

def clear():
    t.clear()
    t.teleport(0,0)
screen.listen()
screen.onkeyrelease(fun=move_forward,key="w")
screen.onkeyrelease(fun=move_right,key="d")
screen.onkeyrelease(fun=move_back,key="s")
screen.onkeyrelease(fun=move_left,key="a")
screen.onkeyrelease(fun = clear,key = 'c')
screen.exitonclick()


