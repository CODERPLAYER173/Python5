from tkinter import *

from Python5.Gema_quiz.main import question_text


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
        self.Score = Label(self.root, text=f"score:{self.score}",fg="black")
        self.Score.grid(row=0, column=1)
        #canvas
        self.canvas = Canvas(self.root)
        self.canvas.config(height = 200, width = 375, bg="white")
        self.canvas.place(x=7, y=100)
        mainloop()
    def show_question(self):
        self.canvas.itemconfig(text= question_text)

quiz = QuizUI()