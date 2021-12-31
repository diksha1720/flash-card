from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
time = None
flag = 0


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
    global flag
    global new_list
    flag = 1
    reset_timer()
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(title, text="ENGLISH", fill="white")
    english = data[data["French"] == french].values[0][1]
    canvas.itemconfig(word, text=english, fill="white")


def next_word():
    global new_list
    global flag
    global french
    if flag == 0:
        new_list = [word_info for word_info in new_list if word_info["French"] != french]
        # print(new_list)
    flag = 0
    if len(new_list) == 0:
        reset_timer()
        messagebox.showinfo(title="Congratulations!!", message="You finished all the words")
    else:
        reset_timer()
        start_timer(5)
        canvas.itemconfig(canvas_img, image=front_img)
        canvas.itemconfig(title, text="FRENCH", fill="black")
        french = random.choice(new_list)["French"]
        canvas.itemconfig(word, text=french, fill="black")
        score = 101 - len(new_list)
        canvas.itemconfig(current_score, text=f"Score : {score}/100")


data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)


window = Tk()
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR, highlightthickness=0)
window.title("Flash Card")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas_img = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 180, text="FRENCH", fill="black", font=("Helvetica", 30, "italic"), )
french = random.choice(data_dict)["French"]
new_list = [word_info for word_info in data_dict ]
word = canvas.create_text(400, 320, text=french, fill="black", font=("Times New Roman", 40, "bold"), )
current_score = canvas.create_text(400, 30, text="score : 0/100", fill="black", font=("Times New Roman", 25, "bold"))
canvas.grid(column=0, row=1, columnspan=2)

r_button = Button(image=right_img, highlightthickness=0, command=next_word)
r_button.grid(column=1, row=2)

w_button = Button(image=wrong_img, highlightthickness=0, command=english_meaning)
w_button.grid(column=0, row=2)

timer_text = Label(text="", fg="black", bg=BACKGROUND_COLOR,  font=("Helvetica", 20, "bold"), highlightthickness=0)
timer_text.grid(column=0, row=3, columnspan=2)

start_timer(5)

window.mainloop()
