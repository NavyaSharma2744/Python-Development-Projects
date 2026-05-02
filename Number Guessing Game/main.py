import customtkinter as ctk
import random

# Appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Game variables
number = random.randint(1, 1000)
attempts = 0
max_attempts = 30


def check_guess():
    global attempts

    user_input = entry.get()

    if not user_input.isdigit():
        result_label.configure(text="❌ Write an integer please")
        return

    guess = int(user_input)

    if not (1 <= guess <= 1000):
        result_label.configure(text="❌ Enter number between 1–1000")
        return

    attempts += 1
    attempts_label.configure(text=f"Attempts: {attempts}/{max_attempts}")

    # Out of attempts
    if attempts >= max_attempts and guess != number:
        result_label.configure(
            text=f"❌ You ran out of chances! Number was {number}"
        )
        button.configure(state="disabled")
        return

    # Correct guess
    if guess == number:
        if attempts <= 5:
            performance = "🌟 Excellent!"
        elif attempts <= 20:
            performance = "🔥 Great!"
        else:
            performance = "👍 Good!"

        result_label.configure(
            text=f"🎉 Correct! Number was {number}\nAttempts: {attempts}/{max_attempts}\n{performance}"
        )
        button.configure(state="disabled")
        return

    # Too high
    elif guess > number:
        if guess - number > 20:
            result_label.configure(text="Too high ⬆")
        else:
            result_label.configure(text="Slightly high ⬆")

    # Too low
    else:
        if number - guess > 20:
            result_label.configure(text="Too low ⬇")
        else:
            result_label.configure(text="Slightly low ⬇")


def reset_game():
    global number, attempts

    number = random.randint(1, 1000)
    attempts = 0

    attempts_label.configure(text=f"Attempts: 0/{max_attempts}")
    result_label.configure(text="")

    entry.delete(0, "end")
    button.configure(state="normal")


# UI
app = ctk.CTk()
app.title("Number Guessing Game")
app.geometry("400x380")

title = ctk.CTkLabel(app, text="Guess Number (1–1000)", font=("Arial", 20))
title.pack(pady=15)

attempts_label = ctk.CTkLabel(app, text=f"Attempts: 0/{max_attempts}")
attempts_label.pack(pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Enter your guess")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Check", command=check_guess)
button.pack(pady=10)

# 🔁 Replay button
reset_button = ctk.CTkButton(app, text="Play Again 🔄", command=reset_game)
reset_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=20)

app.mainloop()