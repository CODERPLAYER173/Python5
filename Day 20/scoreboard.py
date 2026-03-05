from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("Documents/Highscore.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.teleport( x = 0,y= 280)
        self.write(arg=f'Scoreboard:   {self.score} High score: {self.highscore}',move = False,align="center",font=("Arial",20,"bold"))
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Scoreboard:   {self.score} High score: {self.highscore}', move=False, align="center", font=("Arial", 20, "bold"))
    def reset_high(self):
        if self.score >self.highscore:
            self.highscore = self.score
            with open("Documents/Highscore.txt", mode="w") as file:
                file.write(f'{self.highscore}')
    def game_over(self):
        self.color("White")
        self.teleport(x=0,y=0)
        self.write(arg='GAMEOVER!!!!!!', move=False, align="center", font=("Arial", 20, "bold"))



