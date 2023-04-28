import tkinter

window = tkinter.Tk()

window.title("Tkinter Test")

window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="This is test", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

my_label["text"] = "new test"
my_label.config(text="new test", padx=50, pady=50)


# Button

new_button = tkinter.Button(text= "new button")
new_button.grid(row= 0, column= 2)
def button_clicked():
    my_label.config(text=f"개추{input.get()}")


button = tkinter.Button(text="어이 '클릭'해라", command=button_clicked)
button.grid(row=1, column=1)

# Entry(입력)

input = tkinter.Entry(width=30)
input.grid(row=2, column=3)

# text

window.mainloop()
