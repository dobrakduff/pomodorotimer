from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="TIMER")
    check_mark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 ==0:
        cont_down(long_break_sec)
        title.config(text="break",fg=RED)
    elif reps % 2 ==0:
        cont_down(short_break_sec)
        title.config(text="break", fg=PINK)
    else:
        cont_down(work_sec)
        title.config(text="work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def cont_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,cont_down,count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)




title = Label(text="TIMER",bg=YELLOW,fg=GREEN,highlightthickness=0,font=(FONT_NAME,35,"bold"))

title.grid(row=0,column=1)


canvas = Canvas(width=200,height=234, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


button_start = Button(text="START", command=start_timer, highlightthickness=0)
button_start.grid(row=2,column=0)

button_reset = Button(text="RESET", command=reset,highlightthickness=0)
button_reset.grid(row=2,column=2)

check_mark = Label(text= "",fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)




window.mainloop()
