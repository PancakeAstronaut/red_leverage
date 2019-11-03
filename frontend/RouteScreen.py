from tkinter import *
from pymsgbox import *
from frontend import Login
from frontend import RouteInfo
from frontend import alert
from frontend import view_weather


def editOptions():
    def plan():                   # functions to handle option box choices
        frontend.withdraw()
        RouteInfo.info()

    def view():
        frontend.withdraw()
        view_weather.view_weather()

    def alerts():
        frontend.withdraw()
        alert.alerts()

    def log_out():
        x = confirm(text="Are you sure you want to Log Out?", title="Confirm Log Out",
                   buttons=['Yes', 'No'])
        if x == 'Yes':
            frontend.withdraw()
            Login.main()
        else:
            pass

    def submit_choice():                # evaluates chose option from option box
        choice = choicevar.get()
        if choice == option1:
            plan()
        elif choice == option2:
            view()
        elif choice == option3:
            alerts()
        elif choice == option4:
            log_out()
        else:
            warning = confirm(text="You have to choose an option to continue.", title="Woah There!",
                              buttons=['OK'])
            pass

    def exit_prog():
        exitButton = confirm(text="Are you sure you want to Exit?", title="Confirm Exit",
                             buttons=['Yes', 'No'])
        if exitButton == "Yes":                         # exit confirmation window & validation
            exit()
        else:
            frontend.withdraw()
            editOptions()

    option1 = "Plan your Route"             # values for option box
    option2 = "View Weather"
    option3 = "Alerts"
    option4 = "Log Out"
    frontend = Tk()                         # window instance
    frontend.columnconfigure(0, weight=1)
    frontend.columnconfigure(3, weight=1)
    frontend.title("Geico Weather Advisor")
    frontend.rowconfigure(0, weight=1)
    frontend.rowconfigure(5, weight=1)
    frontend.configure(background='lightblue')
    promptbox_lbl = Label(frontend, text="What would you like to do?: ")
    promptbox_lbl.grid(column=2, row=2)
    choicevar = StringVar(frontend)
    choicevar.set("Select an Option")
    menu = OptionMenu(frontend, choicevar, option1, option2, option3, option4)      # option box
    menu.grid(column=2, row=3)
    submit = Button(frontend, text="Submit", command=submit_choice)     # calls function at Line: 26
    submit.grid(column=2, row=4)
    submit.config(height=2, width=8)
    exit_btn = Button(frontend, text="Quit", command=exit_prog)         # calls function at Line: 37
    exit_btn.grid(column=2, row=5)
    exit_btn.config(height=2, width=6)
    btn_padding = Label(frontend, bg='lightblue', text="\n\n")
    btn_padding.grid(column=2, row=1)
    paddingleft = Label(frontend, bg='lightblue', text="                      ")
    paddingleft.grid(column=1, row=0)
    paddingright = Label(frontend, bg='lightblue', text="                      ")
    paddingright.grid(column=3, row=0)
    paddingfloor = Label(frontend, bg='lightblue', text="\n\n\n")
    paddingfloor.grid(column=2, row=7)
    frontend.mainloop()


if __name__ == '__main__':                       # file wont run endlessly once called with this here.
    editOptions()           # calls function on Line: 9