import turtle as turtle
import pandas
from turtle import Turtle,Screen
text = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
a = pandas.read_csv("50_states.csv")
location_x = a["x"].tolist()
location_y = a["y"].tolist()
b = turtle.textinput("guess the State ","What is the name of the specific state")
state = a["state"].tolist()
if  b in state:
    text.hideturtle()
    text.teleport()
print(a[(b[1])])
turtle.mainloop()
