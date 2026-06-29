import tkinter as tk

window = tk.Tk()
window.title("HANGMAN GAME")
window.geometry("600x500")

word = "elephant"
guessed_letters = []
wrong_guesses = 0
max_tries = 6
hints = [
    "It is an animal",
    "It is big in size",
    "It is a mammal",
    "It has a trunk",
    "It has large ears",
    "It is grey in colour"
]
hint_index = 0

def display_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def draw_hangman():
    if wrong_guesses == 1:
        canvas.create_oval(150, 50, 200, 100)
    elif wrong_guesses == 2:
        canvas.create_line(175, 100, 175, 200)
    elif wrong_guesses == 3:
        canvas.create_line(175, 120, 140, 160)
    elif wrong_guesses == 4:
        canvas.create_line(175, 120, 210, 160)
    elif wrong_guesses == 5:
        canvas.create_line(175, 200, 140, 250)
    elif wrong_guesses == 6:
        canvas.create_line(175, 200, 210, 250)

def check_letter():
    global wrong_guesses, tries
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if guess in word:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            message_label.config(text="Good job!", fg="green")
        else:
            message_label.config(text="Already guessed!", fg="orange")
    else:
        wrong_guesses += 1
        tries -= 1
        message_label.config(text="Wrong! Try again.", fg="red")
        draw_hangman()

    word_label.config(text=display_word())
    tries_label.config(text=f"You have {tries} tries left")

    if "_" not in display_word():
        message_label.config(text="You Win!", fg="green")
    elif tries == 0:
        message_label.config(text="Game Over! Word was: " + word, fg="red")

def show_hint():
    global hint_index, tries, wrong_guesses

    if hint_index < len(hints) and tries > 0:
        hint_label.config(text="💡 " + hints[hint_index])
        hint_index += 1
        tries -= 1
        wrong_guesses += 1
        draw_hangman()
        tries_label.config(text=f"You have {tries} tries left")

    if tries == 0:
        message_label.config(text="Game Over! Word was: " + word, fg="red")

def StartGame():
    for widget in window.winfo_children():
        widget.destroy()

    global guessed_letters, wrong_guesses, hint_index, tries
    guessed_letters = []
    wrong_guesses = 0
    hint_index = 0
    tries = 6

    global hint_label, word_label, entry, message_label, canvas, tries_label

    hint_button = tk.Button(window, text="💡 Hint", command=show_hint)
    hint_button.pack(pady=5)

    hint_label = tk.Label(window, text="", font=("Arial", 12))
    hint_label.pack()

    tries_label = tk.Label(window, text="You have 6 tries", font=("Arial", 12))
    tries_label.pack(pady=5)

    word_label = tk.Label(window, text=display_word(), font=("Arial", 22))
    word_label.pack(pady=20)

    entry = tk.Entry(window)
    entry.pack(pady=10)

    submit_button = tk.Button(window, text="Submit", command=check_letter)
    submit_button.pack(pady=5)

    message_label = tk.Label(window, text="", font=("Arial", 12))
    message_label.pack(pady=10)

    canvas = tk.Canvas(window, width=300, height=300)
    canvas.pack()

title_label = tk.Label(window, text="HANGMAN GAME", font=("Arial", 25, "bold"), bg="black", fg="white")
title_label.pack(pady=20)

start_button = tk.Button(window, text="PRESS TO START!", command=StartGame)
start_button.pack(pady=20)

window.mainloop()
