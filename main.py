from tkinter import *
from tkinter.ttk import *
from playsound import playsound
import math
import threading

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    text.config(text='Timer', foreground=GREEN)
    check.config(text='')
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        threading.Thread(target=alarm).start()
        pop_up()
        text.config(text="Break", foreground=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        threading.Thread(target=alarm).start()
        pop_up()
        text.config(text="Break", foreground=PINK)
        count_down(short_break_sec)
    else:
        text.config(text="Work", foreground=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'

    if minutes < 10:
        minutes = f'0{minutes}'

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()
        check.config(text="✓" * math.floor(REPS / 2))


# ---------------------------- POP UP --------------------------------- #

def alarm():
    playsound('alarm.wav')


# ---------------------------- POP UP --------------------------------- #
def pop_up():
    window.lift()
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Tracker')
window.config(padx=25, pady=25, bg=YELLOW)

style = Style()
style.configure('TButton', font=(FONT_NAME, 10, 'bold'), borderwidth='2')

text = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), background=YELLOW, foreground=GREEN)
text.grid(row=0, column=1)

canvas = Canvas(width=220, height=240, background=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(105, 125, image=image)
timer_text = canvas.create_text(105, 145, text="00:00", fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text='Start', width=10, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', width=10, command=reset_timer)
reset.grid(row=2, column=2)

check = Label(font=(FONT_NAME, 15, 'bold'), background=YELLOW, foreground=GREEN)
check.grid(row=3, column=1)

window.mainloop()
