import math
from PIL import Image, ImageTk
from tkinter import *
print(TkVersion)
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
work_session = 0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps
    reps += 1
    if reps %8==0:
        count_down(LONG_BREAK_MIN*60)
        title.config(text="Long Break",fg = RED)
    elif reps % 2 != 0 :
      count_down(WORK_MIN*60)
      title.config(text="Work",fg = GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        title.config(text="Short Break",fg = PINK)
    elif reps %2 != 0 and reps != 1:
        checkmark = Label(pady=20, text="✔", fg=GREEN, bg=YELLOW, font=("Arial", 40, "bold"))
        checkmark.grid(row=3, column=2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global work_session
    min = math.floor(count/60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec <= 9:
        sec = f"0{sec}"



    canvas.itemconfig(tt,text =f'{min}:{sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        timer_start()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(height=224,width=200)
canvas.config(bg=YELLOW,highlightthickness=0)


title = Label(text="TIMER",fg=GREEN,bg=YELLOW, font=("Arial",35,"bold"))
title.grid(row = 0,column= 2)
a = PhotoImage(file = "/Users/dheerajsrivastava/Documents/GitHub/Python13/pomodoro-start/tomato.png")


canvas.create_image(100, 112,image =a)
tt = canvas.create_text(100,130,text ="00:00",fill="white", font=("Arial",40,"bold"))
canvas.grid(row=2,column=2)
button1 = Button(text = "Start",highlightthickness=0,command=timer_start)

button1.grid(row = 3,column = 1)
button2 = Button(text="Reset",highlightthickness=0)

button2.grid(row=3,column=3)


mainloop()