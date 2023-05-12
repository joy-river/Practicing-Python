BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas

def change_word():
    canvas.itemconfig(french_word, text= random.choice(read_data)["French"])
    window.after(3000, flip)

def flip():
    global current_front
    if current_front:


    canvas.create_image()

window = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

current_front = True
canvas.create_image(400, 263, image=front_image)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Placeholder", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

read_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


Button(image=correct_image, highlightthickness=0, command=change_word).grid(row=1, column=1)
Button(image=wrong_image, highlightthickness=0, command=change_word).grid(row=1, column=0)


window.mainloop()
