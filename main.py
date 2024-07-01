from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

screen = Tk()
screen.title("Flash Cards")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashCardImage = PhotoImage(file="./images/card_front.png")
remember = PhotoImage(file="./images/right.png")
forget = PhotoImage(file="./images/wrong.png")


flashCard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashCard.create_image(400, 263, image=flashCardImage)
flashCard.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
flashCard.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
flashCard.grid(row=0, column=0, columnspan=2)


rememberButton = Button(image=remember, highlightthickness=0)
rememberButton.grid(row=1, column=0)
forgetButton = Button(image=forget, highlightthickness=0)
forgetButton.grid(row=1, column=1)


screen.mainloop()
