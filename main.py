from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
french_words = []
english_words = []


def french_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_img, image=front_img)
    card = random.choice(data_dict)
    canvas.itemconfig(first, text="French", fill="black")
    word = card["French"]
    canvas.itemconfig(second, text=word, fill="black")

    flip_timer = window.after(3000, func=english_card)


def english_card():
    eng_word = card["English"]
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(first, text="English", fill="white")
    canvas.itemconfig(second, text=eng_word, fill="white")
    french_words.append(card["French"])
    english_words.append(card["English"])
    words_to_learn_dict = {
        "French": french_words,
        "English": english_words
    }
    words_to_learn = pandas.DataFrame(words_to_learn_dict)
    words_to_learn.to_csv("words_to_learn.csv", index=False)


def is_know():
    data_dict.remove(card)
    print(len(data_dict))
    french_card()



window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=english_card)
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=8, row=8, columnspan=2)

first = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
second = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
wrong_img = PhotoImage(file="images/wrong.png")
wrg_button = Button(image=wrong_img, highlightthickness=0, command=french_card)
wrg_button.grid(column=7, row=10)
right_img = PhotoImage(file="images/right.png")
ryt_button = Button(image=right_img, highlightthickness=0, command=is_know)
ryt_button.grid(column=10, row=10)
data = pandas.read_csv("data/french_words.csv")

# data_dict ={row.French: row.English for(index, row) in data.iterrows()}
data_dict = data.to_dict(orient="records")
# french_words = [data_dict[i]["French"] for i in range(len(data_dict))]
# english_words = [data_dict[i]["English"] for i in range(len(data_dict))]
french_card()



window.mainloop()
