"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random

def test_random():
    random_number = random.randint(1, 20)
    return random_number

num = test_random()
attempts = 6
print("=== SIMPLE GUESSING GAME ===\nGuess my number between 1 and 20!\nYou have 6 attempts.")
for attempt in range(attempts):
    num_user = int(input(f"\nAttempt {attempts}/6 - Enter your guess: "))
    if num_user == num:
        print(f"Congratulations! You won in {attempt} attempts!")
        break
    elif num_user > num:
        print("Too high! Try again.")
        attempts -= 1
    elif num_user < num:
        print("Too low! Try again.")
        attempts -= 1

    if attempts == 0:
        print("Sorry, Your attempt is over.")

