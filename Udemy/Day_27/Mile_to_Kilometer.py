import tkinter as tk

window = tk.Tk()

window.title("Mile to Km")
window.config(padx=20, pady=20)

convert = 0

entry = tk.Entry(width=10)
entry.grid(row=0, column=1)

label_mile = tk.Label(text="Mile")
label_mile.grid(row=0, column=2)

label_equal = tk.Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_convert = tk.Label(text="0")
label_convert.grid(row=1, column=1)

label_kilo = tk.Label(text="Km")
label_kilo.grid(row=1, column=2)


def calculate():
    mile_kilo = (int(entry.get()) * 9 / 5) + 32
    label_convert.config(text= f"{mile_kilo}")


button_cal = tk.Button(text="Calculate", command=calculate)
button_cal.grid(row=2, column=1)

window.mainloop()
