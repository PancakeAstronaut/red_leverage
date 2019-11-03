from tkinter import *

lWindow = Tk()
lWindow.title("Login")

lWindow.columnconfigure(0, weight=1)
lWindow.rowconfigure(0, weight=1)
lWindow.configure(background="Light Blue")

lblHead = Label(lWindow, text="Login", bg="Light Blue", fg="Blue", font="none 40 bold")
lblHead.grid(column=1, row=0)

lblEmail = Label(lWindow, text="Username:", bg="Light Blue")
lblEmail.grid(column=0, row=1)

entEmail = Entry(lWindow, width=45)
entEmail.grid(column=1, row=1, columnspan=1)

lblPassword = Label(lWindow, text="Password", bg="Light Blue")
lblPassword.grid(column=0, row=2)

entPassword = Entry(lWindow, show="*", width=45)
entPassword.grid(column=1, row=2, columnspan=2)

btnLogin = Button(lWindow, text="Login")
btnLogin.grid(column=1, row=3)
btnLogin.config(height=2, width=10)

btnCancel = Button(lWindow, text="Cancel")
btnCancel.grid(column=1, row=4)
btnCancel.config(height=2, width=10)




lWindow.mainloop()