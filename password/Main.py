
from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#functions
def Save():
    password = Password.get()
    website = Website.get()
    email = Email.get()
    fn = "Newfile.csv"
    data = ([{"Website name": website,"Email address": email,"Password": password}])
    d = pd.DataFrame(data)
    d.to_excel(fn, index=False, header=False)
    print(d)


def password_generator():
    passsword = ""
    for l in range(1, 7 + 1):
        passsword += (random.choice(letters))

    for l in range(1, 2 + 1):
        passsword += (random.choice(numbers))

    for l in range(1, 2 + 1):
        passsword += (random.choice(symbols))
    Password.insert(0,passsword)

#ui setup
root  = Tk()
root.config(bg="white")
root.minsize(width=1000,height=1000)




img = ImageTk.PhotoImage(Image.open("logo.png"))
canvas = Canvas(height=200,width=190)
canvas.config(bg="white",highlightthickness=0)
canvas.create_image(100, 95, image=img)
canvas.place(x =350,y =200)



website = Label(text="Website Name:")
website.config(bg="white",font=("arial",15,"normal"))
website.place(x=200,y=500)
Website = Entry()
Website.config(width=45)
Website.place(x =350,y =500)



email = Label(text="Email address:")
email.config(bg="white",font=("arial",15,"normal"))
email.place(x=200,y=550)
Email = Entry()
Email.config(width=45)
Email.place(x =350,y =550)


password = Label(text="Password")
password.config(bg="white",font=("arial",15,"normal"))
password.place(x=200,y=600)
Password =Entry()
Password.config(width=20)
Password.place(x =350,y =600)



generate = Button(text="Generate Password",command=password_generator)
generate.config(bg="white",highlightbackground="white",fg="black",height=1,width=12)
generate.place(x=600,y=600)


save = Button(text="SAVE",command=Save)
save.config(bg="white",highlightbackground="white",fg="black",height=1,width=45)
save.place(x=350,y=650)
mainloop()




