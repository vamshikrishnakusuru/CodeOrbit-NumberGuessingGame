"""
CodeOrbit Tech Python Programming Internship
Task 3: Number Guessing Game

Description:
An interactive, beginner-friendly command-line Number Guessing Game.
The computer selects a random secret number, and the player receives
dynamic feedback ('Too High' / 'Too Low') until guessing correctly.
Includes attempt tracking, difficulty selection, and multiple rounds.

Author: CodeOrbit Tech Intern
Language: Python 3
"""

import random


def generate_number(min_val=1, max_val=100):
    """
    Generate and return a random secret integer between min_val and max_val.
    Keeps the number hidden from the player.
    """
    return random.randint(min_val, max_val)


def select_difficulty():
    """
    Allow the player to select a game difficulty level.
    Returns a tuple of (min_val, max_val, difficulty_name).
    """
    difficulties = {
        "1": (1, 50, "Easy (1-50)"),
        "2": (1, 100, "Medium (1-100)"),
        "3": (1, 200, "Hard (1-200)")
    }

    print("\nSelect Difficulty Level:")
    print("  1. Easy   (Range: 1 to 50)")
    print("  2. Medium (Range: 1 to 100) [Default]")
    print("  3. Hard   (Range: 1 to 200)")

    while True:
        choice = input("Enter difficulty (1-3) [Press Enter for Medium]: ").strip()

        # Default to Medium if user presses Enter
        if choice == "":
            return difficulties["2"]

        try:
            if choice in difficulties:
                return difficulties[choice]
            else:
                raise ValueError("Invalid option selected.")
        except ValueError:
            print("  [!] Error: Please select a valid difficulty level (1, 2, or 3).")


def get_player_guess(min_val, max_val):
    """
    Prompt the player for an integer guess and validate with try-except.
    Rejects non-numeric entries and values outside the allowed range.
    """
    while True:
        user_input = input(f"Enter your guess ({min_val}-{max_val}): ").strip()

        try:
            # Convert user input to an integer
            guess = int(user_input)

            # Check if the number is within the allowed range
            if min_val <= guess <= max_val:
                return guess
            else:
                print(f"  [!] Error: Out of range! Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            # Handle non-numeric input gracefully
            print("  [!] Error: Invalid input! Please enter a valid whole number.")


def get_performance_rating(attempts):
    """
    Return an encouraging feedback message based on the total number of attempts.
    """
    if attempts == 1:
        return "Unbelievable! Hole-in-one on your very first try! Pure genius!"
    elif attempts <= 4:
        return "Impressive! Excellent deduction and intuition!"
    elif attempts <= 7:
        return "Great job! That was a solid guessing strategy!"
    elif attempts <= 10:
        return "Good effort! You narrowed it down nicely!"
    else:
        return "You got it! Keep practicing to beat your personal best!"


def play_game():
    """
    Execute a single round of the Number Guessing Game.
    Tracks attempts, provides hints, and displays performance summary.
    """
    # 1. Select difficulty level
    min_val, max_val, diff_name = select_difficulty()
    secret_number = generate_number(min_val, max_val)

    print("\n" + "=" * 45)
    print(f"  Difficulty: {diff_name}")
    print(f"  I have selected a secret number between {min_val} and {max_val}.")
    print("  Can you guess what it is?")
    print("=" * 45 + "\n")

    attempts = 0

    # 2. Guessing loop
    while True:
        guess = get_player_guess(min_val, max_val)
        attempts += 1

        # 3. Provide guessing hints
        if guess > secret_number:
            print("  [-] Too High! Try again.\n")
        elif guess < secret_number:
            print("  [+] Too Low! Try again.\n")
        else:
            # 4. Correct guess congratulations
            print("\n" + "*" * 45)
            print("  CONGRATULATIONS! YOU GUESSED IT! ")
            print("*" * 45)
            print(f"  The secret number was: {secret_number}")
            print(f"  Total attempts taken:  {attempts}")
            print(f"  Rating: {get_performance_rating(attempts)}")
            print("*" * 45)
            break


def main():
    """
    Main application loop for the Number Guessing Game.
    Allows players to enjoy multiple consecutive rounds.
    """
    print("\n" + "#" * 50)
    print("    WELCOME TO THE NUMBER GUESSING GAME!    ")
    print("#" * 50)
    print("Rules:")
    print("1. Guess the secret number chosen by the computer.")
    print("2. You'll receive 'Too High' or 'Too Low' hints after every guess.")
    print("3. Try to find the secret number in the fewest attempts possible!")

    round_number = 1

    while True:
        print(f"\n>>> Starting Round #{round_number} <<<")
        play_game()

        # 5. Multiple rounds query
        print("\n" + "-" * 45)
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("\n" + "=" * 50)
            print("  Thank you for playing! See you next time. Goodbye!")
            print("=" * 50 + "\n")
            break

        round_number += 1


if __name__ == "__main__":
    main()
