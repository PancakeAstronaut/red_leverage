from tkinter import *

suWindow = Tk()
suWindow.title("Sign Up")

suWindow.columnconfigure(0, weight=1)
suWindow.rowconfigure(0, weight=1)
suWindow.configure(background="Light Blue")

lblHead = Label(suWindow, text="Sign Up", bg="Light Blue", fg="Blue", font="none 40 bold")
lblHead.grid(column=1, row=0)

lblName = Label(suWindow, text="Full Name: ", bg="Light Blue")
lblName.grid(column=0, row=1)

entName = Entry(suWindow, width=45)
entName.grid(column=1, row=1)

lblEmail = Label(suWindow, text="Email Address: ", bg="Light Blue")
lblEmail.grid(column=0, row=2)

entEmail = Entry(suWindow, width=45)
entEmail.grid(column=1, row=2)

lblAddress = Label(suWindow, text="Address: ", bg="Light Blue")
lblName.grid(column=0, row=3)

entAddress = Entry(suWindow, width=45)
entAddress.grid(column=1, row=3)

lblCity = Label(suWindow, text="City: ", bg="Light Blue")
lblCity.grid(column=0, row=4)

entCity = Entry(suWindow, width=45)
entCity.grid(column=1, row=4)

suWindow.mainloop()