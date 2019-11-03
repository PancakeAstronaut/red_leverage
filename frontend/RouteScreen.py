from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

rsWindow = Tk()

#Working title
rsWindow.title("Plan Your Route")
rsWindow.columnconfigure(0, weight=1)
rsWindow.rowconfigure(0, weight=1)

#cbValues = StringVar()

# cbSelect = ttk.Combobox(rsWindow, state='readonly', values=[
#     "Select your option",
#     "Plan your Route",
#     "View Current",
#     "Alerts",
#     "Logout"])
# print(dict(cbSelect))
# cbSelect.grid(column=1, row=0)
# cbSelect.current(0)
#
# cbBtn = Button(rsWindow, text="Select")
# cbBtn.grid(column=1, row=1)

cbSelect = Combobox()
cbSelect['values'] = ("Select your option", "Plan your Route", "View Current", "Alerts", "Logout")
cbSelect.current(0)
cbSelect.grid(column=1, row=0)


def theclick():

    if cbSelect.get() == "Plan your Route":
        lblStarting = Label(rsWindow, text="Starting Location")
        lblStarting.grid(column=1, row=2)

        entStarting = Entry(rsWindow, width=45)
        entStarting.grid(column=1, row=3)

        lblDestination = Label(rsWindow, text="Destination")
        lblDestination.grid(column=1, row=4)

        entDestination = Entry(rsWindow, width=45)
        entDestination.grid(column=1, row=5)

        # lblAdd = Label(rsWindow, text="Add a Location")

        btnAdd = Button(rsWindow, text="Add Another Location")
        btnAdd.grid(column=1, row=6)
        #btnAdd.config(height=2, width=15)

        btnGo = Button(rsWindow, text="Start")
        btnGo.grid(column=1, row=7)
       # btnGo.config(height=2, width=15)

    if cbSelect.get() == "View Current":
        lblTest1 = Label(rsWindow,text="Current Information")
        lblTest1.grid(column=1, row=2)

        lblCurrentInfo = Label(rsWindow, text="Placeholder info")
        lblCurrentInfo.grid(column=1, row=3)
    if cbSelect.get() == "Alerts":
        lblAlerts = Label(rsWindow, text="Current Alerts")
        lblAlerts.grid(column=1, row=2)

        lblnewAlerts = Label(rsWindow, text="Placeholder")
        lblnewAlerts.grid(column=1, row=3)
    if cbSelect.get() == "Logout":
        #something goes here
        print("")

# cbSelect.bind("<<ComboBoxSelected>>", callbackFunc)


cbSelectBtn = Button(rsWindow, text="Select", command=theclick)
cbSelectBtn.grid(column=1, row=1)

rsWindow.mainloop()
