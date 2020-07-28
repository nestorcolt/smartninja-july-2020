from tkinter import messagebox
from project.game import game
import importlib
import tkinter
import random

importlib.reload(game)

# Lesson 008
##############################################################################################
# User Interface with TKinter

ATTEMPTS = 0
SECRET = random.randint(1, 30)


def check_guess():
    if guess.get() == "":
        messagebox.showinfo("ERROR",
                            "Guess info should be an integer or not be empty.\nCheck guess input field and try again.")
        return

    # Make reference to global variable
    global ATTEMPTS
    ATTEMPTS += 1

    game.get_game_data()
    message = game.play_game(guess=int(guess.get()), player=player.get(), secret=SECRET, attempts=ATTEMPTS)

    # game info window
    messagebox.showinfo("Game Info", message)

    # Closes main window if the secret number is correct
    if SECRET == int(guess.get()):
        window.destroy()
        return

    # clean up text field widgets
    guess.delete(0, "end")


##############################################################################################
# window logic starts here
window = tkinter.Tk()
window.geometry("350x350")

# greeting text
greeting = tkinter.Label(window, text="Guess the secret number!", font=("Helvetica", 18), pady=35)
greeting.pack()

instructions = tkinter.Label(window, text="Enter a number between 1 and 30", font=("Helvetica", 12), pady=10)
instructions.pack()

# player name text
player_name_label = tkinter.Label(window, text="Player Name:")
player_name_label.pack()

# player entry field
player = tkinter.Entry(window)
player.pack()

# player name text
guess_label = tkinter.Label(window, text="Enter Guess:")
guess_label.pack()

# guess entry field
guess = tkinter.Entry(window)
guess.pack()

spacer = tkinter.Label(window, text="\n---------------------------------------------\n", pady=5)
spacer.pack()

# submit button
submit = tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()

# launch window
window.mainloop()

##############################################################################################
