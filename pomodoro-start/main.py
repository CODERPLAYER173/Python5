from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(height=224,width=200)
canvas.config(bg=YELLOW,highlightthickness=0,)
title = Label(text="TIMER")
title.config(fg=GREEN,bg=YELLOW, font=("Arial",35,"bold"))
title.grid(row = 0,column= 2)
a =  PhotoImage(file = "tomato.png")
canvas.create_image(100, 112,image =a)
canvas.create_text(100,130,text ="00:00",fill="white", font=("Arial",40,"bold"))
canvas.grid(row=2,column=2)
button1 = Button(text = "Start")
button1.grid(row = 3,column = 1)
button2 = Button()
mainloop()