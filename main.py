from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def get_data():
    global to_learn
    try:
        data = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("./data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")

    return to_learn


to_learn = get_data()
current_card = {}


def flip_card():
    flashCard.itemconfig(card_title, text="English", fill="white")
    flashCard.itemconfig(card_word, text=current_card["English"], fill="white")
    flashCard.itemconfig(card_image, image=card_back_img)


def next_card():
    global current_card, timer
    screen.after_cancel(timer)
    current_card = choice(to_learn)
    flashCard.itemconfig(card_title, text="French", fill="black")
    flashCard.itemconfig(card_word, text=current_card["French"], fill="black")
    flashCard.itemconfig(card_image, image=card_front_img)
    timer = screen.after(3000, func=flip_card)


def remember_word():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


screen = Tk()
screen.title("Flashy")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = screen.after(3000, func=flip_card)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
remember = PhotoImage(file="./images/right.png")
forget = PhotoImage(file="./images/wrong.png")


flashCard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = flashCard.create_image(400, 263, image=card_front_img)
flashCard.grid(row=0, column=0, columnspan=2)

card_title = flashCard.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = flashCard.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))


rememberButton = Button(image=remember, highlightthickness=0, command=remember_word)
rememberButton.grid(row=1, column=1)
forgetButton = Button(image=forget, highlightthickness=0, command=next_card)
forgetButton.grid(row=1, column=0)

next_card()


screen.mainloop()
