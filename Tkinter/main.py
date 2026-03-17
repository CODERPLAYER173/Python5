from tkinter import *
window = Tk()
window.minsize(width=200,height=150)

label = Label(text="Miles")
label.grid(row=0,column=2)
text =  Label(text="is equal to")
text.grid(row = 2,column = 0)
Input = Entry()
Input.grid(row=0,column = 1)
Input.config(width=5)
km =  Label(text= Input.get())

km.grid(row=2,column=1)
def button():
    label["text"] = Input.get()
button1 = Button(text="Click me", command=button)
button1.grid(row = 3,column=4)
window.mainloop()
