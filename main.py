from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# --reding csv--
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# -- next card func --
after_id = None
current_card = {}


def next_card():
    global current_card, after_id
    if after_id:
        window.after_cancel(after_id)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_front, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    after_id = window.after(3000, flip_card)


# -- flip card func --
def flip_card():
    canvas.itemconfig(card_front, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# window.after_cancel(task)

# ---GUI---
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_front = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()
# window.after(3000, waithere)

window.mainloop()
