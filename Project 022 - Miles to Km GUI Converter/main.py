from tkinter import *

ONE_MILE_TO_KM = 1.609344

window = Tk()
window.title("Converter App")
window.config(width=200, height=200, pady=20, padx=20)


def calculate():
    """Calculates miles to kms"""
    miles = int(input_box.get())
    kms = ONE_MILE_TO_KM * miles
    l_answer.config(text=kms)


# input box
input_box = Entry()
input_box.grid(row=0, column=1)
input_box.insert(END, string="0")

# miles label
l_miles = Label(text="miles", font=("Arial", 12, "normal"))
l_miles.grid(row=0, column=2)

# is equal to label
l_is_equal_to = Label(text="is equal to ", font=("Arial", 12, "normal"))
l_is_equal_to.grid(row=1, column=0)

# answer label
l_answer = Label(text="0 ", font=("Arial", 14, "normal"))
l_answer.grid(row=1, column=1)

# km label
l_km = Label(text="Km", font=("Arial", 12, "normal"))
l_km.grid(row=1, column=2)

# calculate button
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
