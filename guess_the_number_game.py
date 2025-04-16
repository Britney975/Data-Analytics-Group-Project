#guess_the_number_game.py
import random

class NumberGuessGame:
    """Handles logic for the Number Guess Game."""

    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.max_attempts = 7
        self.attempts = 0
        self.score = 0

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess (1-100): "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def play_round(self):
        print("\n--- Welcome to the Number Guess Game! ---")
        self.attempts = 0  # Reset attempts for each new round
        self.secret_number = random.randint(1, 100)  # Reset the secret number for each round
        while self.attempts < self.max_attempts:
            guess = self.get_user_guess()
            self.attempts += 1

            if guess == self.secret_number:
                print(f"Congrats! You've guessed the number {self.secret_number} in {self.attempts} tries.")
                self.score = 100 - (self.attempts * 10)
                break
            elif guess < self.secret_number:
                print("Too low!")
            else:
                print("Too high!")

        if self.score == 0:
            print(f"\nYou ran out of attempts! The number was {self.secret_number}.")
        print(f"Your score for this round: {self.score}")
        return self.score

    def play_game(self):
        """This function allows the user to play multiple rounds."""
        while True:
            self.play_round()
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break

# Run the game
if __name__ == "__main__":
    game = NumberGuessGame()
    game.play_game()

      