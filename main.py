from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
time = None


def start_timer(count):
    global time
    timer_text.config(text=count)
    if count > 0:
        time = window.after(1000, start_timer, count-1)
    if count <= 0:
        english_meaning()


def reset_timer():
    global time
    timer_text.config(text=" ")
    window.after_cancel(time)


def english_meaning():
    reset_timer()
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(title, text="ENGLISH", fill="white")
    english = data[data["French"] == french].values[0][1]
    canvas.itemconfig(word, text=english, fill="white")


def next_word():
    global french
    reset_timer()
    start_timer(5)
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(title, text="FRENCH", fill="black")
    french = random.choice(french_words)
    canvas.itemconfig(word, text=french, fill="black")


data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict()
french_words = data["French"].to_list()

window = Tk()
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR, highlightthickness=0)
window.title("Flash Card")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas_img = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 140, text="FRENCH", fill="black", font=("Helvetica", 30, "italic"), )
french = random.choice(french_words)
word = canvas.create_text(400, 300, text=french, fill="black", font=("Times New Roman", 40, "bold"), )
canvas.grid(column=0, row=0, columnspan=2)

r_button = Button(image=right_img, highlightthickness=0, command=next_word)
r_button.grid(column=1, row=1)

w_button = Button(image=wrong_img, highlightthickness=0, command=english_meaning)
w_button.grid(column=0, row=1)

timer_text = Label(text="", fg="black", bg=BACKGROUND_COLOR,  font=("Helvetica", 30, "bold"), highlightthickness=0)
timer_text.grid(column=0, row=2, columnspan=2)

start_timer(5)

window.mainloop()
