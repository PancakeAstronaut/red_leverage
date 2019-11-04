from tkinter import *
from pymsgbox import *
from backend import route_data
from frontend import RouteInfo


def arb():
    print("")


def enterinfo():

    def exit_func():
        exitButton = confirm(text="Are you sure you want to Exit?", title="Confirm Exit",
                             buttons=['Yes', 'No'])
        if exitButton == "Yes":                         # exit confirmation window & validation
            exit()
        else:
            pass

    def submit():
        startpoint = entStarting.get()
        endpoint = entDestination.get()
        if startpoint == " ":
            tmp = route_data.get_current_location()
            start = tmp[0]
        else:
            start = startpoint
        if endpoint == " ":
            entStarting.delete(first=0, last=45)
            entDestination.delete(first=0, last=45)
            confirm(text="Destination cannot be Null", title="Null Value Exception", buttons=['OK'])

        riWindow.withdraw()
        RouteInfo.info(start, endpoint)

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

    btnsubmit = Button(riWindow, text="Submit", command=submit)
    btnsubmit.grid(column=1, row=6)
    btnexit = Button(riWindow, text="Exit", command=exit_func)

    riWindow.mainloop()
    #go


if __name__ == '__main__':
    arb()
