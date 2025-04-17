import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors")
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        self.rock_button = tk.Button(self.buttons_frame, text="🪨 Rock", width=10, command=lambda: self.play("rock"))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.buttons_frame, text="📄 Paper", width=10, command=lambda: self.play("paper"))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.buttons_frame, text="✂️ Scissors", width=10, command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Your Score: 0 | Computer Score: 0")
        self.score_label.pack()

    def play(self, user_choice):
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        outcome = self.determine_winner(user_choice, computer_choice)

        if outcome == "win":
            self.user_score += 1
            result_text = f"You chose {user_choice}, computer chose {computer_choice}. You win!"
        elif outcome == "lose":
            self.computer_score += 1
            result_text = f"You chose {user_choice}, computer chose {computer_choice}. You lose!"
        else:
            result_text = f"You both chose {user_choice}. It's a draw!"

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")

    def determine_winner(self, user, computer):
        if user == computer:
            return "draw"
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            return "win"
        else:
            return "lose"

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()