from tkinter import *

gWindow = Tk()
gWindow.title("Working Title")

gWindow.columnconfigure(0, weight=1)
gWindow.rowconfigure(0, weight=1)
gWindow.configure(background="Light Blue")

lblHead = Label(gWindow, text="Working Title", bg="Light Blue", fg="Blue", font="none 48 bold")
lblHead.grid(column=0, row=0)

btnLogin = Button(gWindow, text="Login")
btnLogin.grid(column=0, row=4)
btnLogin.config(height=2, width=10)

btnSignUp = Button(gWindow, text="Sign Up")
btnSignUp.grid(column=0, row=6)
btnSignUp.config(height=2, width=10)

btnGuest = Button(gWindow, text="Guest")
btnGuest.grid(column=0, row=8)
btnGuest.config(height=2, width=10)

gWindow.mainloop()
