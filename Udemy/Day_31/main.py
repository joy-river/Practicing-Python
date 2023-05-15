BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas

dict_word = {}
def next_word():
    global dict_word, win_id
    window.after_cancel(win_id)
    dict_word = random.choice(read_data)
    canvas.itemconfig(image, image=front_image)
    canvas.itemconfig(text_lang, text="French", fill="black")
    canvas.itemconfig(text_word, text=dict_word["French"], fill="black")
    win_id = window.after(3000, flip)


def flip():
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfig(text_lang, text="English", fill="white")
    canvas.itemconfig(text_word, text=dict_word["English"], fill="white")


def correct():
    global dict_word, win_id
    read_data.remove(dict_word)
    df = pandas.DataFrame({"French": [item["French"] for item in read_data],
                           "English": [item["English"] for item in read_data]})
    df.to_csv("data/data_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

win_id = window.after(3000, flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

try:
    read_data = pandas.read_csv("data/data_to_learn.csv").to_dict(orient="records")
except:
    read_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

current_front = False
image = canvas.create_image(400, 263)
text_lang = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

Button(image=correct_image, highlightthickness=0, command=correct).grid(row=1, column=1)
Button(image=wrong_image, highlightthickness=0, command=next_word).grid(row=1, column=0)

next_word()


window.mainloop()
