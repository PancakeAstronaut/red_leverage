from tkinter import *
from pymsgbox import *
from frontend import Login
from backend import dbConn


def create_acct():

    def create_user():
        username = entName.get()
        password = entPassword.get()
        email = entEmail.get()
        ind = dbConn.sql_injection(username=username, password=password, email=email)
        if ind == 0:
            confirm(text="Account could not be made....\nPlease try again in a minute....",
                    buttons=['OK'])
            entName.delete(first=0, last=45)
            entPassword.delete(first=0, last=45)
            entEmail.delete(first=0, last=45)
        else:
            confirm(text="Account Successfully Created", title="Success", buttons=['OK'])
            suWindow.withdraw()
            Login.main()

    def go_back():
        conf = confirm(text="Are you sure you want go return?", title="Return to Menu?",
                       buttons=['Yes', 'No'])
        if conf == 'Yes':
            suWindow.withdraw()
            Login.main()
        else:
            pass

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

    btnSignUp = Button(suWindow, text="Sign Up", command=create_user)
    btnSignUp.grid(column=1, row=6)
    btnSignUp.config(height=2, width=10)

    btnCancel = Button(suWindow, text="Cancel", command=go_back)
    btnCancel.grid(column=1, row=7)
    btnCancel.config(height=2, width=10)

    suWindow.mainloop()


if __name__ == '__main__':
    create_acct()
