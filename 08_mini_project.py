"""
LESSON 8: Mini Project - Number Guessing Game
=============================================
Time to combine everything: variables, input, conditionals, loops,
functions, and error handling.

The game:
  1. The computer picks a random number between 1 and 100.
  2. The player keeps guessing.
  3. After each guess, say "Too high!" or "Too low!".
  4. When they get it, say how many guesses it took.

Fill in the TODOs, then run:  python 08_mini_project.py

NEW IDEAS in this file:
  - `import random` loads a module (extra tools that come with Python)
  - try/except catches errors so the program doesn't crash
  - `if __name__ == "__main__":` means "only run this when the file is run directly"
"""
import random

# Example of try/except: int("abc") would normally crash with ValueError
try:
    number = int("abc")
except ValueError:
    print("(example) 'abc' is not a number, but we didn't crash!\n")


def get_guess():
    """Ask the player for a number until they type a valid one, then return it."""
    while True:
        text = input("Your guess: ")
        # TODO: try to convert `text` to an int and return it.
        # If it fails (ValueError), print "Please type a whole number." and
        # let the loop ask again.
        pass


def check_guess(guess, secret):
    """Return "high", "low", or "correct"."""
    # TODO: compare guess with secret and return the right word.
    pass


def play():
    secret = random.randint(1, 100)   # random whole number from 1 to 100
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    # TODO: write a loop that:
    #   - gets a guess with get_guess()
    #   - adds 1 to attempts
    #   - uses check_guess() to print "Too high!" or "Too low!"
    #   - when correct, prints f"You got it in {attempts} guesses!" and stops the loop


def main():
    play()
    # STRETCH GOALS (once the basic game works):
    #   1. Ask "Play again? (y/n)" and loop if they say y.
    #   2. Keep track of the best (lowest) score across games.
    #   3. Let the player choose a difficulty that changes the range (1-10, 1-100, 1-1000).
    #   4. Give the player a maximum number of guesses.


if __name__ == "__main__":
    main()
