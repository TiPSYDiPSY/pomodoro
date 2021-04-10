from tkinter import *
from tkinter.ttk import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro method')
window.config(padx=25, pady=25, bg=YELLOW)

style = Style()
style.configure('TButton', font=(FONT_NAME, 10, 'bold'), borderwidth='2')

text = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), background=YELLOW, foreground=GREEN)
text.grid(row=0, column=1)

canvas = Canvas(width=220, height=240, background=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(105, 125, image=image)
canvas.create_text(105, 145, text="00:00", fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text='Start', width=10)
start.grid(row=2, column=0)

reset = Button(text='Reset', width=10)
reset.grid(row=2, column=2)

check = Label(text="✓", font=(FONT_NAME, 15, 'bold'), background=YELLOW, foreground=GREEN)
check.grid(row=3, column=1)

window.mainloop()
