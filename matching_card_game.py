import tkinter as tk
import random
import time
from tkinter import messagebox

class MatchingCardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Matching Card Game")
        self.root.configure(bg="#4B0082")

        self.difficulty_time = {"Easy": 1000, "Medium": 600, "Hard": 300}
        self.grid_sizes = {
            "3x4": (3, 4),
            "4x4": (4, 4),
            "4x5": (4, 5),
            "5x6": (5, 6),
            "8x8": (8, 8),
            "8x12": (8, 12)
        }

        self.emoji_pool = ["🍎", "🍌", "🍇", "🍉", "🍓", "🍒", "🍑", "🥝", "🥥", "🍍", "🥕", "🌽", "🥔", "🍅",
                           "🥦", "🧄", "🧅", "🍞", "🧀", "🍗", "🍖", "🍤", "🍩", "🍪", "🍰", "🎂", "🍫", "🍬",
                           "🍭", "🍯", "🥜", "🍹", "🍺", "🍻", "🥂", "🍵", "🍼", "🥤", "🧃", "🍽️", "🍴",
                           "🥄", "🔪", "🧊", "🥢", "🥡", "🥠", "🧁"]

        self.first_card = None
        self.lock = False
        self.matched = 0
        self.tries = 0
        self.start_time = None

        self.setup_menu()

    def setup_menu(self):
        self.menu_frame = tk.Frame(self.root, bg="#4B0082")
        self.menu_frame.pack(pady=20)

        tk.Label(self.menu_frame, text="Select Difficulty", bg="#4B0082", fg="white", font=("Arial", 14)).pack()
        self.difficulty_var = tk.StringVar(value="Easy")
        for diff in self.difficulty_time.keys():
            tk.Radiobutton(self.menu_frame, text=diff, variable=self.difficulty_var, value=diff,
                           bg="#4B0082", fg="white", selectcolor="#800080").pack()

        tk.Label(self.menu_frame, text="Select Grid Size", bg="#4B0082", fg="white", font=("Arial", 14)).pack(pady=(10, 0))
        self.grid_var = tk.StringVar(value="4x4")
        for size in self.grid_sizes.keys():
            tk.Radiobutton(self.menu_frame, text=size, variable=self.grid_var, value=size,
                           bg="#4B0082", fg="white", selectcolor="#800080").pack()

        tk.Button(self.menu_frame, text="Start Game", command=self.start_game,
                  bg="#800080", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

    def start_game(self):
        self.menu_frame.destroy()
        self.create_game_board()

    def create_game_board(self):
        self.frame = tk.Frame(self.root, bg="#808080")
        self.frame.pack()

        grid_size = self.grid_sizes[self.grid_var.get()]
        rows, cols = grid_size
        total_cards = rows * cols

        if total_cards % 2 != 0:
            messagebox.showerror("Error", "Grid must have an even number of cards.")
            return

        self.matched = 0
        self.tries = 0
        self.start_time = time.time()

        # Status bar
        self.status = tk.Label(self.root, text="Tries: 0 | Time: 0s", font=("Arial", 12),
                               bg="#4B0082", fg="white")
        self.status.pack(pady=5)

        self.cards = {}
        self.buttons = {}
        self.total_pairs = total_cards // 2
        symbols = random.sample(self.emoji_pool, self.total_pairs) * 2
        random.shuffle(symbols)

        for r in range(rows):
            for c in range(cols):
                symbol = symbols.pop()
                btn = tk.Button(self.frame, text="❓", width=4, height=2, font=("Arial", 12, "bold"),
                                command=lambda r=r, c=c: self.reveal_card(r, c), bg="#D8BFD8")
                btn.grid(row=r, column=c, padx=1, pady=1)
                self.cards[(r, c)] = symbol
                self.buttons[(r, c)] = btn

        self.update_timer()

    def update_timer(self):
        if self.matched < self.total_pairs:
            elapsed = int(time.time() - self.start_time)
            self.status.config(text=f"Tries: {self.tries} | Time: {elapsed}s")
            self.root.after(1000, self.update_timer)

    def reveal_card(self, r, c):
        if self.lock or self.buttons[(r, c)]["text"] != "❓":
            return

        self.buttons[(r, c)]["text"] = self.cards[(r, c)]
        self.buttons[(r, c)].update()

        if not self.first_card:
            self.first_card = (r, c)
        else:
            r1, c1 = self.first_card
            r2, c2 = r, c
            self.tries += 1

            if self.cards[(r1, c1)] == self.cards[(r2, c2)]:
                self.matched += 1
                self.first_card = None
                if self.matched == self.total_pairs:
                    self.show_end_screen()
            else:
                self.lock = True
                delay = self.difficulty_time[self.difficulty_var.get()]
                self.root.after(delay, lambda: self.hide_cards(r1, c1, r2, c2))

    def hide_cards(self, r1, c1, r2, c2):
        self.buttons[(r1, c1)]["text"] = "❓"
        self.buttons[(r2, c2)]["text"] = "❓"
        self.first_card = None
        self.lock = False

    def show_end_screen(self):
        self.frame.destroy()
        self.status.destroy()

        end_frame = tk.Frame(self.root, bg="#4B0082")
        end_frame.pack(pady=100)

        time_taken = int(time.time() - self.start_time)
        tk.Label(end_frame, text=f"🎉 You won in {self.tries} tries and {time_taken} seconds! 🎉",
                 font=("Arial", 16, "bold"), bg="#4B0082", fg="white").pack(pady=20)

        tk.Button(end_frame, text="Play Again", command=lambda: self.restart_game(end_frame),
                  bg="#800080", fg="white", font=("Arial", 12, "bold"), width=15).pack(pady=5)

        tk.Button(end_frame, text="Exit", command=self.root.destroy,
                  bg="#800080", fg="white", font=("Arial", 12, "bold"), width=15).pack(pady=5)

    def restart_game(self, frame):
        frame.destroy()
        self.setup_menu()


if __name__ == "__main__":
    root = tk.Tk()
    app = MatchingCardGame(root)
    root.mainloop()
