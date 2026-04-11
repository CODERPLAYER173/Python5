from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
def Save():
    import smtplib
    import datetime as dt
    password = Password.get()
    email = str(Email.get())
    email2 = str(REmail.get())
    now = dt.datetime.now()
    a = (now.day, now.month)
    b = (Date.get())
    print(a)
    if a == b:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(from_addr=email,to_addrs=email2,msg="yoo")
        print("yoo")



root  = Tk()
root.config(bg="white")
root.minsize(width=1000,height=1000)




img = ImageTk.PhotoImage(Image.open("moew.png"))
canvas = Canvas(height=400,width=380)
canvas.config(bg="white",highlightthickness=0)
canvas.create_image(100, 190, image=img)
canvas.place(x =350,y =200)



website = Label(text="Name of the person ")
website.config(bg="white",font=("arial",15,"normal"))
website.place(x=200,y=500)
Website = Entry()
Website.config(width=45)
Website.place(x =350,y =500)

email1 = Label(text="Your Email address:")
email1.config(bg="white",font=("arial",15,"normal"))
email1.place(x=180,y=550)
Email = Entry()
Email.config(width=45)
Email.place(x =350,y =550)

remail = Label(text="Person's Email address:")
remail.config(bg="white",font=("arial",15,"normal"))
remail.place(x=175,y=600)
REmail = Entry()
REmail.config(width=45)
REmail.place(x =350,y =600)


password = Label(text="App Password")
password.config(bg="white",font=("arial",15,"normal"))
password.place(x=200,y=650)
Password =Entry()
Password.config(width=20)
Password.place(x =350,y =650)


date = Label(text="Date")
date.config(bg="white",font=("arial",15,"normal"))
date.place(x=200,y=700)
Date =Entry()
Date.insert(0, " Enter in numbers  : Day,month")
Date.config(width=20)
Date.place(x =350,y =700)



save = Button(text="SAVE",command=Save)
save.config(bg="white",highlightbackground="white",fg="black",height=1,width=45)
save.place(x=350,y=750)
mainloop()

#main function 




