from tkinter import *
from tkinter import ttk

rsWindow = Tk()

rsWindow.title("Plan Your Route")
rsWindow.columnconfigure(0, weight=1)
rsWindow.rowconfigure(0, weight=1)

cbSelect = ttk.Combobox(rsWindow, values=[
    "Select your option",
    "Plan your Route",
    "View Current",
    "Alerts"
    "Logout"])
print(dict(cbSelect))
cbSelect.grid(column=1, row=0)
cbSelect.current(1)



def callbackFunc(event):
    if cbSelect == "Plan your Route":
        lblStarting = Label(rsWindow, text="Starting Location")
        lblStarting.grid(column=1, row=1)

        entStarting = Entry(rsWindow, width=45)
        entStarting.grid(column=1, row=2)

        lblDestination = Label(rsWindow, text="Destination")
        lblDestination.grid(column=1, row=3)

        entDestination = Entry(rsWindow, width=45)
        entDestination.grid(column=1, row=4)

        #lblAdd = Label(rsWindow, text="Add a Location")

        btnAdd = Button(rsWindow, text="Add Another Location")
        btnAdd.grid(column=1, row=5)
        btnAdd.config(height=2, width=15)

        btnGo = Button(rsWindow, text="Start")
        btnGo.grid(column=1, row=6)
        btnGo.config(height=2, width=15)
    if cbSelect == "View Current":
        lblTest1 = Label(rsWindow,text="made it")
        lblTest1.grid(column=2,row=2)



cbSelect.bind("<<ComboBoxSelected>>", callbackFunc)

rsWindow.mainloop()