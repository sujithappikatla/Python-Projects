from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
language_data = ""
pick = ""
timer = ""


def read_data():
    global language_data
    try:
        language_data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        language_data = pandas.read_csv("data/french_words.csv")
    finally:
        language_data = language_data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(img, image=bg_img)
    canvas.itemconfig(lang, text="English")
    canvas.itemconfig(word, text=f"{ pick['English'] }")


def pick_random_word():
    global pick, timer
    pick = random.choice(language_data)
    canvas.itemconfig(img, image=fg_img)
    canvas.itemconfig(lang, text="French")
    canvas.itemconfig(word, text=f"{pick['French']}")
    canvas.itemconfig(to_learn, text=f"Words to  learn : {len(language_data)}")
    timer = window.after(3000, flip_card)


def wrong_click():
    window.after_cancel(timer)
    pick_random_word()


def right_click():
    global language_data
    window.after_cancel(timer)
    language_data.remove(pick)
    df = pandas.DataFrame(language_data)
    df.to_csv("data/words_to_learn.csv", index=False)
    pick_random_word()


# window
window = Tk()
window.title("Flash Card App")
window.config(padx=40, pady=30, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
fg_img = PhotoImage(file="images/card_front.png")
bg_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=fg_img)
canvas.grid(row=0, column=0, columnspan=2)

# language label
lang = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))

# language word
word = canvas.create_text(400, 253, text="trouve", font=("Arial", 60, "bold"))

# words to learn
to_learn = canvas.create_text(150, 450, text="Words to  learn : 0", font=("Arial", 18, "italic"))

# wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, relief=GROOVE, borderwidth=0)
wrong_button.config(command=wrong_click)
wrong_button.grid(row=1, column=0)

# right button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, relief=GROOVE, borderwidth=0)
right_button.config(command=right_click)
right_button.grid(row=1, column=1)

read_data()
pick_random_word()

window.mainloop()
