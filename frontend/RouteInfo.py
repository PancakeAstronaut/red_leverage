from tkinter import *
from pymsgbox import *
from frontend import RouteScreen
from backend import route_data
from backend import evaluate_weather


def arb():
    print("")


def info(start, endpoint):

    def ex_it():
        x = confirm(text="Are you sure you want to Exit?", title="Exit?", buttons=['Yes', 'No'])
        if x == 'Yes':
            frame.withdraw()
            exit()
        else:
            pass

    def restart_program():
        x = confirm(text="Are you sure you want to go back?", title="Go Back?", buttons=['Yes', 'No'])
        if x == 'Yes':
            frame.withdraw()
            RouteScreen.editOptions()
        else:
            pass
    frame = Tk()
    frame.title("Canvas API Information Application")
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.configure(background='blue')
    side_padding_l = Label(frame, bg='blue', text="                      ")
    side_padding_l.grid(column=0, row=0)
    side_padding_r = Label(frame, bg='blue', text="                      ")
    side_padding_r.grid(column=5, row=0)
    back_btn = Button(frame, text="Go Back", command=restart_program)
    back_btn.config(height=2, width=8)
    back_btn.grid(column=2, row=0)
    exit_btn = Button(frame, text="Exit", command=ex_it)
    exit_btn.config(height=2, width=8)
    exit_btn.grid(column=4, row=0)
    distances = route_data.get_Distances(start, endpoint)
    coordinates = route_data.get_Coordinates(start, endpoint)
    addresses = route_data.get_Addresses(start, endpoint)
    durations = route_data.get_Duration(start, endpoint)
    cur_rpt = evaluate_weather.eval_current_loc(coordinates[0])
    dest_rpt = evaluate_weather.eval_dest_weather(coordinates[1])
    current_report = evaluate_weather.create_rpt(cur_rpt)
    dest_report = evaluate_weather.create_rpt(dest_rpt)
    emp_lbl = Text(frame)
    emp_lbl.insert(END, "To: {}\nFrom: {}\nDuration: {}\nDistance: {}\n".format(addresses[0], addresses[1], str(durations[0]) + durations[1], str(distances[0]) + distances[1]))
    emp_lbl.insert(END, "Current Location Weather:\n{}".format(current_report))
    emp_lbl.insert(END, "Destination Weather:\n{}".format(dest_report))
    emp_lbl.grid(column=3, row=2)
    frame.mainloop()


if __name__ == '__main__':
    arb()