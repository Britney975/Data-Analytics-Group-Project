from guess_the_movie_gui import start_guess_movie
import tkinter as tk
from tkinter import messagebox

# Placeholder functions for your games
def start_charades():
    start_guess_movie()

def start_snake():
    messagebox.showinfo("Tic-Tac-Toe", "Launching Tic-Tac-Toe game...")

def start_tic_tac_toe():
    messagebox.showinfo("Tic-Tac-Toe", "Launching Tic-Tac-Toe game...")

def show_help():
    messagebox.showinfo("Help", "Instructions or game help goes here.")

def exit_game():
    root.destroy()

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
btn_snake = tk.Button(menu_frame, text="Number Guessing", width=20, command=start_snake, bg="#FFFF00", fg="black", font=("Arial", 12, "bold")) # Yellow
btn_tic = tk.Button(menu_frame, text="Tic-Tac-Toe", width=20, command=start_tic_tac_toe, bg="#3CB371", fg="white", font=("Arial", 12, "bold")) # Medium Sea Green
btn_help = tk.Button(menu_frame, text="Help", width=20, command=show_help, bg="#1E90FF", fg="white", font=("Arial", 12, "bold")) # Dodger Blue
btn_exit = tk.Button(menu_frame, text="Exit", width=20, command=exit_game, bg="#DC143C", fg="white", font=("Arial", 12, "bold"))   # Crimson

btn_charades.pack(pady=5, fill="x")
btn_snake.pack(pady=5, fill="x")
btn_tic.pack(pady=5, fill="x")
btn_help.pack(pady=5, fill="x")
btn_exit.pack(pady=5, fill="x")

root.mainloop()