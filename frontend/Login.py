from tkinter import *
from pymsgbox import *
from frontend import SignUp
from backend import dbConn
from frontend import GridMainMenu


def main():

    def create():
        app.withdraw()
        SignUp.create_acct()

    def login():
        username = entuname.get()
        password = entPassword.get()
        validator = dbConn.credentials_validator(username, password)
        if validator[0] == 0:
            entuname.delete(first=0, last=45)
            entPassword.delete(first=0, last=45)
            confirm(text="Credentials invalid/not found....\nTry again!", title="Credentials Issue",
                    buttons=['OK'])
        elif username == str(validator[0]) and password == str(validator[1]):
            app.withdraw()
            GridMainMenu.main_menu()
        else:
            entuname.delete(first=0, last=45)
            entPassword.delete(first=0, last=45)
            confirm(text="Data Source Error", title="Error 404 ",
                    buttons=['OK'])

    def exit_func():
        conf = confirm(text="Are you sure you sure you want to Exit?", title="Exit Confirmation",
                       buttons=['Yes', 'No'])
        if conf == 'Yes':
            app.withdraw()
            exit()
        else:
            pass

    app = Tk()
    app.title("Log In to [Service]")
    app.configure(background="lightblue")
    # window padding
    top_padding = Label(app, bg="lightblue", text="\n\n")
    top_padding.grid(column=5, row=0)
    floor_padding = Label(app, bg="lightblue", text="\n\n")
    floor_padding.grid(column=5, row=15)
    right_pading = Label(app, bg="lightblue", text="                  ")
    right_pading.grid(column=10, row=0)
    left_padding = Label(app, bg="lightblue", text="                  ")
    left_padding.grid(column=0, row=0)
    # window content
    title = Label(app, bg="lightblue", fg='blue', font="none 40 bold", text="Welcome! \n Please Log In!\n")
    title.grid(column=5, row=4)
    lbluname = Label(app, text="Username: ", bg="Light Blue")
    lbluname.grid(column=5, row=5)
    entuname = Entry(app, width=45)
    entuname.grid(column=5, row=6)
    lblPassword = Label(app, text="Password: ", bg="Light Blue")
    lblPassword.grid(column=5, row=7)
    entPassword = Entry(app, show="*", width=45)
    entPassword.grid(column=5, row=8)
    # buttons
    btnLogin = Button(app, text="Login", command=login)
    btnLogin.grid(column=5, row=9)
    btnLogin.config(height=2, width=12)
    btnCancel = Button(app, text="Exit", command=exit_func)
    btnCancel.grid(column=5, row=10)
    btnCancel.config(height=2, width=12)
    lbl_create = Label(app, bg="lightblue", text="Don't have an account? Create One!")
    lbl_create.grid(column=5, row=11)
    create_btn = Button(app, text="Create Account", command=create)
    create_btn.grid(column=5, row=12)
    create_btn.config(height=2, width=12)
    app.mainloop()


if __name__ == '__main__':
    main()
