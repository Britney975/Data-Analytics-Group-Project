
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
# Run the game
if __name__ == "__main__":
    game = NumberGuessGame()
    game.play_round()
      