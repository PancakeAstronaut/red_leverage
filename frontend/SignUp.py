from tkinter import *

suWindow = Tk()
suWindow.title("Sign Up")

suWindow.columnconfigure(0, weight=1)
suWindow.rowconfigure(0, weight=1)
suWindow.configure(background="Light Blue")

lblHead = Label(suWindow, text="Sign Up", bg="Light Blue", fg="Blue", font="none 40 bold")
lblHead.grid(column=1, row=0)

lblName = Label(suWindow, text="Username: ", bg="Light Blue")
lblName.grid(column=0, row=1)

entName = Entry(suWindow, width=45)
entName.grid(column=1, row=1)

lblEmail = Label(suWindow, text="Email Address: ", bg="Light Blue")
lblEmail.grid(column=0, row=2)

entEmail = Entry(suWindow, width=45)
entEmail.grid(column=1, row=2)

lblPassword = Label(suWindow, text="Password: ", bg="Light Blue")
lblPassword.grid(column=0, row=4)

entPassword = Entry(suWindow, width=45)
entPassword.grid(column=1, row=4)

terms = Checkbutton(suWindow, text="I agree to Working Names ToS and EULA")
terms.grid(column=1, row=5)

btnSignUp = Button(suWindow, text="Sign Up")
btnSignUp.grid(column=1, row=6)
btnSignUp.config(height=2, width=10)

btnCancel = Button(suWindow, text="Cancel")
btnCancel.grid(column=1, row=7)
btnCancel.config(height=2, width=10)

suWindow.mainloop()
