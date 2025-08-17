import tkinter as tk
import random
from tkinter import messagebox

# Predefined word list
WORDS = ["python", "hangman", "developer", "programming", "internship"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game 🎮")
        self.root.geometry("600x500")
        self.root.config(bg="#2c3e50")  # Dark theme background

        self.title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 24, "bold"),
                                    bg="#2c3e50", fg="#ecf0f1")
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(root, text="", font=("Helvetica", 20, "bold"),
                                   bg="#2c3e50", fg="#f1c40f")
        self.word_label.pack(pady=20)

        self.status_label = tk.Label(root, text="Guess a letter", font=("Helvetica", 14),
                                     bg="#2c3e50", fg="#ecf0f1")
        self.status_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root, bg="#2c3e50")
        self.buttons_frame.pack()

        self.restart_button = tk.Button(root, text="Restart Game 🔄", font=("Helvetica", 14, "bold"),
                                        bg="#27ae60", fg="white", command=self.start_game)
        self.restart_button.pack(pady=20)

        self.start_game()

    def start_game(self):
        self.word = random.choice(WORDS).upper()
        self.hidden_word = ["_"] * len(self.word)
        self.guesses_left = 6

        self.word_label.config(text=" ".join(self.hidden_word))
        self.status_label.config(text=f"Lives left: {self.guesses_left}")

        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Create alphabet buttons
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, height=2,
                            font=("Helvetica", 12, "bold"),
                            bg="#3498db", fg="white",
                            command=lambda l=letter: self.guess(l))
            btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)

    def guess(self, letter):
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i] = letter
            self.word_label.config(text=" ".join(self.hidden_word))
        else:
            self.guesses_left -= 1
            self.status_label.config(text=f"Lives left: {self.guesses_left}")

        if "_" not in self.hidden_word:
            messagebox.showinfo("You Win 🎉", f"Congratulations! The word was {self.word}")
            self.start_game()
        elif self.guesses_left == 0:
            messagebox.showerror("Game Over 💀", f"Oops! You lost. The word was {self.word}")
            self.start_game()


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
