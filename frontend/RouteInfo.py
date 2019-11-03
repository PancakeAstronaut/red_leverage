from tkinter import *


def arb():
    print("")


def info():

    riWindow = Tk()
    riWindow.title("RouteInfo")
    riWindow.columnconfigure(0, weight=1)
    riWindow.rowconfigure(0, weight=1)
    mainHeader = Label(riWindow, text="Route Info", font="none 40 bold")
    mainHeader.grid(column=5, row=0)
    rptbox = Text(riWindow, height=10, width=10)
    rptbox.grid(column=5, row=4)

    lblStarting = Label(riWindow, text="StartingLocation")
    lblStarting.grid(column=1, row=2)

    entStarting = Entry(riWindow, width=45)
    entStarting.grid(column=1, row=3)

    lblDestination = Label(riWindow, text="Destination")
    lblDestination.grid(column=1, row=4)

    entDestination = Entry(riWindow, width=45)
    entDestination.grid(column=1, row=5)

    riWindow.mainloop()


if __name__ == '__main__':
    arb()