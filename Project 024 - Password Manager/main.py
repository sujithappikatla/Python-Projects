from tkinter import *
from tkinter import messagebox
import password_generator as pg
import pyperclip
import json

FONT = "Arial"


# ----------------------------SEARCH --------------------------------------------#

def search():
    website = website_entry.get()
    if not website:
        messagebox.showinfo(title="Empty Field", message="Please Enter Website !!")
        return

    try:
        with open("data.json", "r") as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"{website} does not exist in db")
    else:
        try:
            searched_email = json_data[website]["email"]
            searched_password = json_data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="Error", message=f"{website} does not exist in db")
        else:
            email_entry.delete(0, END)
            email_entry.insert(END, searched_email)
            password_entry.delete(0, END)
            password_entry.insert(END, searched_password)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    random_password = pg.password_generate()
    password_entry.insert(END, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website.strip():
        messagebox.showinfo(title="Empty Field", message="Please Enter Website !!")
        return
    if not email.strip():
        messagebox.showinfo(title="Empty Field", message="Please Enter Email !!")
        return
    if not password.strip():
        messagebox.showinfo(title="Empty Field", message="Please Enter Password !!")
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("data.json", "r") as data_file:
            loaded_data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        loaded_data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(loaded_data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Website label
website_label = Label(text="Website")
website_label.config(font=(FONT, 10))
website_label.grid(row=1, column=0, pady=3, padx=5)

# website entry
website_entry = Entry(highlightthickness=2)
website_entry.config(width=32, bd=0, selectborderwidth=3, highlightbackground="#bbf1fa",
                     highlightcolor="#51c2d5", font=(FONT, 10))
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=1, sticky="W", pady=3)

# Search button
search_button = Button(text="Search")
search_button.config(font=(FONT, 8), borderwidth=2, relief=GROOVE, width=20, command=search)
search_button.grid(row=1, column=2, sticky="W", pady=3, padx=3)

# Email/username label
email_label = Label(text="Email/Username")
email_label.config(font=(FONT, 10))
email_label.grid(row=2, column=0, pady=3, padx=5)

# email/username entry
email_entry = Entry(highlightthickness=2)
email_entry.config(width=45, bd=0, highlightbackground="#bbf1fa", highlightcolor="#51c2d5", font=(FONT, 10))
email_entry.insert(END, "abc@xyz.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="W", pady=3)

# Password label
password_label = Label(text="Password")
password_label.config(font=(FONT, 10))
password_label.grid(row=3, column=0, pady=3, padx=5)

# password entry
password_entry = Entry(highlightthickness=2)
password_entry.config(bd=0, width=32, font=(FONT, 10), highlightbackground="#bbf1fa",
                      highlightcolor="#51c2d5")
password_entry.grid(row=3, column=1, sticky="W", pady=3)

# generate password
password_button = Button(text="Generate Password")
password_button.config(font=(FONT, 8), borderwidth=2, relief=GROOVE, width=20, command=generate_password)
password_button.grid(row=3, column=2, sticky="W", pady=3, padx=3)

# Add button
add_button = Button(text="Add")
add_button.config(width=45, borderwidth=2, relief=GROOVE, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W", pady=3)

window.mainloop()
