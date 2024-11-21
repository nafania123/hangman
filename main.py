import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.words = ["python", "tkinter", "hangman", "programming", "code"]
        self.word = random.choice(self.words)
        self.word_display = ['_' for _ in self.word]
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.label = tk.Label(self.root, text="Guess the word: " + " ".join(self.word_display))
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.bind("<Return>", self.make_guess)

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

    def make_guess(self, event):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if not guess or guess in self.guesses or len(guess) > 1:
            return

        self.guesses.append(guess)
        if guess in self.word:
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_display[index] = guess
        else:
            self.attempts += 1

        self.update_display()

    def update_display(self):
        self.label.config(text="Guess the word: " + " ".join(self.word_display))
        self.message_label.config(text=f"Guesses: {', '.join(self.guesses)}\nAttempts left: {self.max_attempts - self.attempts}")

        if self.attempts >= self.max_attempts:
            self.label.config(text=f"You lost! The word was: {self.word}")
            self.entry.config(state="disabled")
        elif '_' not in self.word_display:
            self.label.config(text=f"You won! The word is: {self.word}")
            self.entry.config(state="disabled")

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
