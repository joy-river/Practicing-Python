# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    result = []
    result += [random.choice(letters) for i in range(0, nr_letters)]
    result += [random.choice(symbols) for i in range(0, nr_symbols)]
    result += [random.choice(numbers) for i in range(0, nr_numbers)]
    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    random.shuffle(result)

    input_password.delete(0, END)
    password = "".join(result)
    pyperclip.copy(password)
    input_password.insert(0, password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    str_tosave = website + "   |   " + email + "  |   " + password + "\n"
    box = messagebox
    is_valid = len(website) > 0 and len(email) > 0 and len(password)

    if is_valid:

        ok = box.askokcancel(title="Are you sure?", message=f"Your password will be saved like this:\n{str_tosave}")

        if ok:
            input_website.delete(0, END)
            input_password.delete(0, END)
            with open(file="saved_password.txt", mode="a") as file:
                file.write(str_tosave)
    else:
        box.showinfo(title="Invalid data", message="One or more of your data is Empty.\nPlease fill up all boxes.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

image_mypass = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image_mypass)
canvas.grid(row=0, column=1)

Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "dlrkd1122@gmail.com")
input_password = Entry(width=19)
input_password.grid(row=3, column=1)

Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
Button(width=36, text="Add", command=add).grid(row=4, column=1, columnspan=2)

window.mainloop()
