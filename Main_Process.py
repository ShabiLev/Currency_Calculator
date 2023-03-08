import time
import tkinter
from programVariables import *
import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox


# get the user's inout for amount if currency to convert
# limit the input to ONLY numbers in float to get the decimal point
def get_user_float_num():
    userfloatnum = tkinter.simpledialog.askfloat('Amount', 'How much do you want to convert?')
    return userfloatnum


def wellcome():
    tkinter.messagebox.showinfo('Currency Converter', 'Wellcome to Currency Converter')


# define the user's options to continue or exit
def get_user_yesno():
    option = tkinter.messagebox.askyesno(
        title='Currency Converter',
        message='Do you want to proceed?',
        default=tkinter.messagebox.YES
    )
    # Continue if YES
    if option:
        log_to_file('User selected YES to continue ')
        what_to_convert()
    # Exit process if NO
    if not option:
        log_to_file('User Exit ')
        option = tkinter.messagebox.askyesno(
            title='Currency Converter',
            message='Thanks for using the Currency converter\nDo you want to see the log file?',
            default=tkinter.messagebox.YES
        )
        # Open Log
        if option:
            time.sleep(1)
            open_log()
            exit(1)
        else:
            tkinter.messagebox.showinfo('Currency Converter', 'Goodbye')
            exit(1)


def what_to_convert():
    message = tk.Tk()
    font = ('times', 14, 'bold')
    message.title('What would you like to convert?')

    w = 350  # width for the Tk root
    h = 300  # height for the Tk root

    # get screen width and height
    ws = message.winfo_screenwidth()  # width of the screen
    hs = message.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen and where it is placed
    message.geometry('%dx%d+%d+%d' % (w, h, x, y))
    message.lift()
    message.attributes('-topmost', True)
    message.attributes('-topmost', False)

    # Define the buttons
    button1 = tk.Button(message,
                        text='ILS To USD',
                        font=font,
                        command=lambda: [f() for f in [message.destroy, ils_to_usd]])
    button1.grid(row=0, column=0, padx=3, pady=30)

    button2 = tk.Button(message,
                        text='ILS To EUR',
                        font=font,
                        command=lambda: [f() for f in [message.destroy, ils_to_eur]])
    button2.grid(row=0, column=1, padx=3, pady=30)

    button3 = tk.Button(message,
                        text='USD To ILS',
                        font=font,
                        command=lambda: [f() for f in [message.destroy, usd_to_ils]])
    button3.grid(row=1, column=0, padx=3, pady=30)

    button4 = tk.Button(message,
                        text='ILS To EUR',
                        font=font,
                        command=lambda: [f() for f in [message.destroy, eur_to_usd]])
    button4.grid(row=2, column=0, padx=3, pady=30)

    button5 = tk.Button(message,
                        text='EUR To ILS',
                        font=font,
                        command=lambda: [f() for f in [message.destroy, eur_to_ils]])
    button5.grid(row=2, column=1, padx=3, pady=30)

    message.mainloop()


# calculation Functions:
def ils_to_usd():
    value_to_convert = get_user_float_num()
    Result = value_to_convert / get_curr_ils_rate()
    log_to_file(f'USer Converted {value_to_convert} ILS to {round(Result, 4)} USD\nWith exchange rate of {get_curr_ils_rate()}')
    messagebox.showinfo('Success!', f'You successfully converted {value_to_convert} ILS to {round(Result, 4)} USD\nWith exchange rate of {get_curr_ils_rate()}')
    get_user_yesno()


def ils_to_eur():
    value_to_convert = get_user_float_num()
    Result = value_to_convert / (get_curr_ils_rate() / get_curr_eur_rate())
    log_to_file(f'USer Converted {value_to_convert} ILS to {round(Result, 4)} EUR\nWith exchange rate of {get_curr_eur_rate()}')
    messagebox.showinfo('Success!', f'You successfully converted {value_to_convert} ILS to {round(Result, 4)}EUR\nWith exchange rate of {get_curr_eur_rate()}')
    get_user_yesno()


def usd_to_ils():
    value_to_convert = get_user_float_num()
    Result = value_to_convert * get_curr_ils_rate()
    log_to_file(f'USer Converted {value_to_convert} USD to {round(Result, 4)} ILS\nWith exchange rate of {get_curr_ils_rate()}')
    messagebox.showinfo('Success!', f'You successfully converted {value_to_convert} USD to {round(Result, 4)} ILS\nWith exchange rate of {get_curr_ils_rate()}')
    get_user_yesno()


def eur_to_usd():
    value_to_convert = get_user_float_num()
    Result = value_to_convert * (get_curr_usd_rate() / get_curr_eur_rate())
    log_to_file(f'USer Converted {value_to_convert} EUR to {round(Result, 4)} USD\nWith exchange rate of {get_curr_usd_rate()}')
    messagebox.showinfo('Success!', f'You successfully converted {value_to_convert} EUR to {round(Result, 4)} USD\nWith exchange rate of {get_curr_usd_rate()}')
    get_user_yesno()


def eur_to_ils():
    value_to_convert = get_user_float_num()
    Result = value_to_convert * (get_curr_ils_rate() / get_curr_eur_rate())
    log_to_file(f'USer Converted {value_to_convert} EUR to {round(Result, 4)} ILS\nWith exchange rate of {get_curr_ils_rate()}')
    messagebox.showinfo('Success!', f'You successfully converted {value_to_convert} EUR to {round(Result, 4)} ILS\nWith exchange rate of {get_curr_ils_rate()}')
    get_user_yesno()
