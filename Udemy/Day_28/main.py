from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label_Timer.config(text="Take a long break.", fg=PINK)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        label_Timer.config(text="Take a short break.", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        label_Timer.config(text="Get your ass back to work.", fg=RED)



def countdown(count):
    if count > 0:
        count_min = int(count / 60)
        count_sec = count % 60
        if count_min < 10:
         count_min = f"0{count_min}"
        if count_sec < 10:
          count_sec = f"0{count_sec}"
        canvas.itemconfig(text, text=f"{count_min}:{count_sec}")
        window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:


            label_check.config(text="✓")




def pressed_reset():
    pass


# ---------------------------- UI SETUP ------------------------------- #
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_Timer = Label()
label_Timer.config(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 40))
label_Timer.grid(row=0, column=1)

button_start = Button()
button_reset = Button()

button_start.config(fg="black", bg=YELLOW, text="Start", command=start_timer)
button_reset.config(fg="black", bg=YELLOW, text="Reset", command=start_timer)

button_start.grid(row=2, column=0)
button_reset.grid(row=2, column=2)

label_check = Label()
label_check.config(fg=GREEN, bg=YELLOW, font=40)
label_check.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
