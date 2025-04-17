from guess_the_movie_gui import start_guess_movie
import tkinter as tk
from tkinter import messagebox

# Placeholder functions for your games
def start_charades():
    start_guess_movie()

def start_match_the_card():
    card_game_start()

def start_whack_a_mole():
    play_whack_a_mole()

def start_rock_paper_scissors():
    play_rock_paper_scissors()

def show_help():
    messagebox.showinfo("Help", "Instructions or game help goes here.")


# Setup main window
root = tk.Tk()
root.title("Master Mind Menu")
root.geometry("400x400")
root.config(bg="#F0E68C")  # Khaki background (similar to the outer area)

# Main frame to hold the menu with a slightly different background
menu_frame = tk.Frame(root, bg="#FAF0E6", padx=20, pady=20) # Light Goldenrod Yellow (similar to the inner area)
menu_frame.pack(pady=20, padx=20)

# Title label
title_bar_frame = tk.Frame(menu_frame,) # Light Blue for the title bar
title_bar_frame.pack(fill="x")

title_icon = tk.Label(title_bar_frame, text="🎮", font=("Arial", 16), bg="#ADD8E6")
title_icon.pack(side="left", padx=5)

title = tk.Label(title_bar_frame, text="Master Mind Menu", font=("Helvetica", 16, "bold"), bg="#ADD8E6", fg="black")
title.pack(pady=10, fill="x")

btn_charades = tk.Button(menu_frame, text="Charades", width=20, command=start_charades, bg="#FF8C00", fg="white", font=("Arial", 12, "bold")) # Dark Orange
btn_mole = tk.Button(menu_frame, text="Whack a mole", width=20, command=start_whack_a_mole, bg="#FFFF00", fg="black", font=("Arial", 12, "bold")) # Yellow
btn_card = tk.Button(menu_frame, text="Match the card", width=20, command=start_match_the_card, bg="#3CB371", fg="white", font=("Arial", 12, "bold")) # Medium Sea Green
btn_RPC = tk.Button(menu_frame, text="Rock Paper Scissors", width=20, command=start_rock_paper_scissors, bg="#DC143C", fg="white", font=("Arial", 12, "bold")) # Medium Sea Green
btn_help = tk.Button(menu_frame, text="Help", width=20, command=show_help, bg="#1E90FF", fg="white", font=("Arial", 12, "bold")) # Dodger Blue

btn_charades.pack(pady=5, fill="x")
btn_mole.pack(pady=5, fill="x")
btn_card.pack(pady=5, fill="x")
btn_RPC.pack(pady=5, fill="x")
btn_help.pack(pady=5, fill="x")

root.mainloop()
