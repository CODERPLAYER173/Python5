import turtle as turtle
import pandas
from turtle import Turtle,Screen
text = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state = data["state"].tolist()
score = 0
guesed_states = []

while score <= 50:

    b = turtle.textinput(f'guess the State your score is {score}', "What is the name of the specific state")
    if b == "Exit":
        not_guessed = [ x for x in state if x not in guesed_states]
        datas = pandas.DataFrame(not_guessed)
        datas.to_csv("Not_guessed.cvs")
        print(not_guessed)
    if  b in state:
        guesed_states.append(b)
        score += 1
        x = data.x[data.state == b].tolist()
        y = data.y[data.state == b].tolist()
        text.hideturtle()
        text.teleport(x[0],y[0])
        text.write(b,move=False,align="center",font=("Arial",20,"bold"))

turtle.mainloop()
