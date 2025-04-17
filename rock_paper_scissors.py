"""
Rock-Paper-Scissors Game with GUI
Author: Saskia Brown
Sources: https://docs.python.org/3/library/tkinter.html, https://realpython.com/python-gui-tkinter/
"""

import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")

        # Scores and stats
        self.user_score = 0
        self.computer_score = 0
        self.total_rounds = 0
        self.total_user_score = 0
        self.user_wins = 0

        self.choices = ["Rock", "Paper", "Scissors"]

        # UI elements
        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=12, command=lambda: self.make_choice("Rock"))
        self.paper_button = tk.Button(self.button_frame, text="Paper", width=12, command=lambda: self.make_choice("Paper"))
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=12, command=lambda: self.make_choice("Scissors"))

        self.rock_button.grid(row=0, column=0, padx=5)
        self.paper_button.grid(row=0, column=1, padx=5)
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, bg="red", fg="white")
        self.reset_button.pack(pady=10)

    def make_choice(self, user_choice):
        computer_choice = random.choice(self.choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
            round_score = 1
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
            self.user_score += 1
            round_score = 3
            self.user_wins += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
            round_score = 0

        self.total_rounds += 1
        self.total_user_score += round_score

        average_score = self.total_user_score / self.total_rounds if self.total_rounds > 0 else 0
        win_percent = (self.user_wins / self.total_rounds) * 100 if self.total_rounds > 0 else 0

        self.result_label.config(
            text=f"{result}\nComputer chose: {computer_choice}\n\n"
                 f"Your Score: {self.user_score}   |   Computer Score: {self.computer_score}\n"
                 f"Rounds Played: {self.total_rounds}\n"
                 f"Avg Score: {average_score:.2f}   |   Win Rate: {win_percent:.1f}%"
        )

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.total_rounds = 0
        self.total_user_score = 0
        self.user_wins = 0
        self.result_label.config(text="")
        self.label.config(text="Game reset! Choose Rock, Paper, or Scissors!")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
