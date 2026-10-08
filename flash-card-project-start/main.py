from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None
to_learn = {}

# ---------------------------- DATA SETUP ------------------------------- #
try:
    # Read the data from the CSV file
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/igbo_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- FLASH CARD LOGIC ------------------------- #
def next_card():
    """pick a random word and updates the flashcard text."""
    global current_card, flip_timer

    # Cancel the previous timer if it exists to avoid staking triggers
    if flip_timer:
        window.after_cancel(flip_timer)

    if not to_learn:
        canvas.itemconfig(card_title, text="Congratulation", fill="white")
        canvas.itemconfig(card_word, text="You learned all the words", fill="white")
        canvas.itemconfig(card_background, image=card_front_img)
        return
    # Pick a random dictionary from the list
    current_card = random.choice(to_learn)

    # Reset UI to the Front (Igbo)
    canvas.itemconfig(card_title, text="Igbo", fill="black")
    canvas.itemconfig(card_word, text=current_card["Igbo"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # Schedule the card to file after 3000ms (3 seconds)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """flip the card to show the English translation."""
    # Update the background to the back image
    canvas.itemconfig(card_background, image=card_back_img)

    # Change text content and set the color to write
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
def is_known():
    """Remove known words from the active list and saves progress to .CSV"""
    if current_card in to_learn:
        to_learn.remove(current_card)

        # Convert the remaining list back to a DataFrame and save to CSV
        new_data = pd.DataFrame(to_learn)
        new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI BUTTONS SETUP -------------------------- #
window = Tk()
window.title("IGBO Flashy".center(250))
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)#, anchor="nw")
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()