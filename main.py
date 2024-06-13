from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PURPLE = "#640D6B"
PINK = "#B51B75"
ORANGE = "#E65C19"
YELLOW = "#F8D082"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=PURPLE)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work Time", fg=ORANGE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif 10 > count_sec > 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro🍅")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), foreground=PURPLE, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=202, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 114, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check_mark = Label(font=(FONT_NAME, 20, "bold"), foreground=ORANGE, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
