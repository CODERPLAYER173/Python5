from tkinter import *



class QuizUI:
    THEME_COLOR = "#375362"
    FONT_NAME = "Arial"

    def __init__(self):
        #window
        self.root = Tk()
        self.root.title("Quiz")
        self.root.minsize(400, 500)
        self.root.config(bg=self.THEME_COLOR)
        #score
        self.score = 0
        self.Score = Label(self.root, text=f"score:{self.score}",fg="white")
        self.Score.grid(row=0, column=1)
        #canvas
        canvas = Canvas(self.root)
        canvas.config(height = 200, width = 400, bg="white")
        canvas.grid(row=3, column=3)
        mainloop()

quiz = QuizUI()