# guess_the_movie_gui.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

MOVIE_DATA = {
    
    "Home Alone.jpg": "Home Alone",
    "avatar.jpg": "Avatar",
    "Venom.jpg": "Venom",
    "Toy Story.jpg": "Toy Story",
    "Shrek.jpg": "Shrek",
    "Moana.jpg": "Moana",
    "Walking Dead.jpg": "Walking Dead",
    "Chucky.jpg": "Chucky",
    "Ted.jpg": "Ted"
}

class GuessTheMovieGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎬 Guess the Movie!")
        self.master.geometry("500x600")
        self.master.configure(bg="#111")

        self.title_label = tk.Label(master, text="Guess the Movie!", font=("Helvetica", 20, "bold"), fg="white", bg="#111")
        self.title_label.pack(pady=10)

        self.image_label = tk.Label(master, bg="#111")
        self.image_label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 14), justify="center")
        self.entry.pack(pady=10)

        tk.Button(master, text="✅ Submit Guess", command=self.check_guess, bg="#28a745", fg="white", font=("Helvetica", 12)).pack(pady=5)
        tk.Button(master, text="🔁 New Image", command=self.load_new_image, bg="#17a2b8", fg="white", font=("Helvetica", 12)).pack(pady=5)
        tk.Button(master, text="📊 Stats", command=self.show_stats, bg="#ffc107", fg="#222", font=("Helvetica", 12)).pack(pady=10)

        self.status_label = tk.Label(master, text="", font=("Helvetica", 12), fg="white", bg="#111")
        self.status_label.pack()

        self.correct = 0
        self.total = 0

        self.load_new_image()

    def load_new_image(self):
        self.entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.filename = random.choice(list(MOVIE_DATA.keys()))
        image_path = os.path.join("images", self.filename)

        image = Image.open(image_path)
        image = image.resize((300, 400))
        self.tk_image = ImageTk.PhotoImage(image)

        self.image_label.config(image=self.tk_image)

    def check_guess(self):
        guess = self.entry.get().strip().lower()
        answer = MOVIE_DATA[self.filename].lower()
        self.total += 1

        if guess == answer:
            self.correct += 1
            self.status_label.config(text="🎉 Correct!", fg="#00ff00")
        else:
            self.status_label.config(text=f"❌ Nope! It was '{MOVIE_DATA[self.filename]}'", fg="#ff4d4d")

    def show_stats(self):
        if self.total == 0:
            msg = "No guesses yet!"
        else:
            accuracy = (self.correct / self.total) * 100
            msg = f"Correct: {self.correct}\nTotal: {self.total}\nAccuracy: {accuracy:.2f}%"
        messagebox.showinfo("📊 Stats", msg)

def start_guess_movie():
    win = tk.Toplevel()
    GuessTheMovieGame(win)
