from tkinter import *

riWindow = Tk()
riWindow.title("RouteInfo")

riWindow.columnconfigure(0, weight=1)
riWindow.rowconfigure(0, weight=1)

mainHeader = Label(riWindow, text="Route Info", font="none 40 bold")
mainHeader.grid(column=1, row=0)

lblEDT = Label(riWindow, text="Estimated Drive Time")
lblEDT.grid(column=0, row=1)

txtEDT = Entry(riWindow, width=10)
txtEDT.grid(column=1, row=1)

lblWC = Label(riWindow, text="Weather Conditions")
lblWC.grid(column=0, row=2)

txtWC = Entry(riWindow, width=10)
txtWC.grid(column=1, row=2)

lblAlerts = Label(riWindow, text="Alerts")
lblAlerts.grid(column=0, row=3)

txtWC = Entry(riWindow, width=10)
txtWC.grid(column=1, row=3)


riWindow.mainloop()