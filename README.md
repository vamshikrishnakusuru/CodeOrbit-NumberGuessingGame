# CodeOrbit Tech - Python Programming Internship

## Task 3: Number Guessing Game

An interactive, beginner-friendly command-line Number Guessing Game written in Python 3. The computer generates a secret random number within a chosen range, and the player receives dynamic hints ("Too High" or "Too Low") after each guess to deduce the secret number in as few attempts as possible.

---

## 📌 Project Overview

This project was developed as part of **Task 3** for the **CodeOrbit Tech Python Programming Internship**. The objective is to demonstrate core Python programming proficiencies including pseudorandom number generation using Python's standard `random` module, modular architecture, input validation, exception handling with `try-except`, and state tracking across multiple rounds.

---

## 📜 Game Rules

1. At the beginning of each round, the player selects a difficulty level (Easy, Medium, or Hard).
2. The computer randomly chooses a secret integer within the corresponding range.
3. The player inputs their guess in the terminal.
4. After each incorrect guess, the game gives immediate feedback:
   - **"Too High! Try again."** if the guess exceeds the secret number.
   - **"Too Low! Try again."** if the guess is below the secret number.
5. When the player guesses the secret number, a victory banner displays the total number of attempts taken and an encouraging performance rating.
6. The player is prompted to start another round or exit gracefully.

---

## ✨ Features

- **Random Secret Number Generation**: Uses `random.randint()` to ensure unpredictable, cryptographically sound pseudorandom selections hidden from the player.
- **Dynamic Difficulty Levels**:
  - 🟢 **Easy**: Range `1 to 50`
  - 🟡 **Medium**: Range `1 to 100` *(Default)*
  - 🔴 **Hard**: Range `1 to 200`
- **Comprehensive Input Validation**:
  - Catches non-numeric entries (letters, symbols, punctuation) using `try-except` blocks.
  - Rejects out-of-range guesses (e.g., guessing `150` in a `1-50` game) without penalty.
- **Accurate Attempt Tracking**: Counts only valid guesses and provides a performance rating at victory.
- **Multi-Round Support**: Seamlessly transitions between consecutive game rounds with fresh secret numbers.
- **Clean Terminal UI**: Formatted banners, readable prompts, and cross-platform compatible output.

---

## 🛠️ Technologies Used

- **Language**: Python 3 (3.8+)
- **Built-in Modules**: `random` (No external packages or dependencies needed)
- **Programming Paradigm**: Modular / Functional Programming

---

## 📋 Requirements & Prerequisites

- **Operating System**: Windows, macOS, or Linux.
- **Python**: Python 3.8 or higher.
- Verify your Python environment:
  ```bash
  python --version
  ```
  *(or `python3 --version` on macOS/Linux)*

---

## 🚀 How to Install and Run

1. **Open your Terminal or PowerShell** and navigate to the project directory:
   ```bash
   cd codeorbit/CodeOrbit_NumberGuessingGame
   ```

2. **Run the Game**:
   ```bash
   python guessing_game.py
   ```
   *(or `python3 guessing_game.py` on macOS/Linux)*

3. **Follow the On-Screen Prompts**:
   - Choose a difficulty level (1-3) or press Enter for default Medium.
   - Enter your guesses until you find the secret number.
   - Choose `yes` to play another round or `no` to exit.

---

## 🎲 Explanation of Core Mechanics

### 1. Random Number Generation (`generate_number`)
```python
def generate_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)
```
- The function relies on Python's built-in `random.randint(a, b)` function.
- It returns an integer $N$ such that $a \le N \le b$ with uniform probability.
- The secret number is kept strictly internal and is never revealed until the player correctly deduces it.

### 2. Attempt Tracking (`attempts`)
- An integer variable `attempts = 0` is initialized at the start of each round.
- Only valid numeric guesses within the allowed range increment the counter:
  ```python
  guess = get_player_guess(min_val, max_val)
  attempts += 1
  ```
- Invalid inputs (e.g. typing `"apple"` or `-5`) do not increment the attempt counter, ensuring fair scoring.
- When the correct number is guessed, `attempts` is used to evaluate the player's performance tier:
  - **1 attempt**: "Unbelievable! Hole-in-one on your very first try!"
  - **2–4 attempts**: "Impressive! Excellent deduction and intuition!"
  - **5–7 attempts**: "Great job! That was a solid guessing strategy!"
  - **8–10 attempts**: "Good effort! You narrowed it down nicely!"
  - **11+ attempts**: "You got it! Keep practicing to beat your personal best!"

---

## 💻 Sample Gameplay Output

```text
##################################################
    WELCOME TO THE NUMBER GUESSING GAME!    
##################################################
Rules:
1. Guess the secret number chosen by the computer.
2. You'll receive 'Too High' or 'Too Low' hints after every guess.
3. Try to find the secret number in the fewest attempts possible!

>>> Starting Round #1 <<<

Select Difficulty Level:
  1. Easy   (Range: 1 to 50)
  2. Medium (Range: 1 to 100) [Default]
  3. Hard   (Range: 1 to 200)
Enter difficulty (1-3) [Press Enter for Medium]: 2

=============================================
  Difficulty: Medium (1-100)
  I have selected a secret number between 1 and 100.
  Can you guess what it is?
=============================================

Enter your guess (1-100): 50
  [-] Too High! Try again.

Enter your guess (1-100): 25
  [+] Too Low! Try again.

Enter your guess (1-100): 37
  [+] Too Low! Try again.

Enter your guess (1-100): 44
  [-] Too High! Try again.

Enter your guess (1-100): 40
  [+] Too Low! Try again.

Enter your guess (1-100): 42

*********************************************
  CONGRATULATIONS! YOU GUESSED IT! 
*********************************************
  The secret number was: 42
  Total attempts taken:  6
  Rating: Great job! That was a solid guessing strategy!
*********************************************

---------------------------------------------
Do you want to play another round? (yes/no): no

==================================================
  Thank you for playing! See you next time. Goodbye!
==================================================
```

---

## 📁 Project Folder Structure

```text
CodeOrbit_NumberGuessingGame/
│
├── guessing_game.py    # Main game script with functions, validation, and game loop
├── .gitignore          # Git ignore configuration for clean tracking
└── README.md           # Complete project documentation and gameplay manual
```

---

## 👤 Author & Acknowledgements

- **Developer**: CodeOrbit Tech Intern
- **Internship**: CodeOrbit Tech Python Programming Internship
- **Task**: Task 3 - Number Guessing Game
