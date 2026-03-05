from turtle import Turtle as Tu


FONT = ("Courier", 24, "normal")


class Scoreboard(Tu):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.teleport(x=-280, y=270)
        self.write(f'Level:{self.level}',False,'left',FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f'Level:{self.level}',False,"left",FONT)


    def game_win(self):
        self.teleport(x=-100,y=0)
        self.write(f'You Win!!!!!!!!!!!!', False, 'left',("Courier", 35, "normal") )

    def game_over(self):
        self.teleport(x=0, y=0)
        self.write(f'game_over', False, 'left', ("Courier", 35, "normal"))