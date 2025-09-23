"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""

import random

def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even" 
    else:
        return "HINT: The number is odd"

def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
    # Return narrowed range around the number
    low = max(current_min, number - 12)
    high = min(current_max, number + 12)
    return f"HINT: The narrowed range around the number is {range(max(current_min, number - 12), min(current_max, number + 12))}"

def get_thefirst_digit_hint(number):
    # Retun the first digit of the number
    result = str(number)
    print(f"HINT: The first digit of the number is {result[0]}")

random_number = random.randint(1, 100)
print("=== Enhanced GUESSING GAME ===\nGuess my number between 1 and 100!\nYou have unlimited attempts.")
attempts = 1
while True:
    num_user = int(input(f"\nAttempt {attempts} - Enter your guess: "))
    if num_user == random_number:
        print(f"Congratulations! You won in {attempts} attempts!")
        break
    elif num_user > random_number:
        print("Too high! Try again.")
    elif num_user < random_number:
        print("Too low! Try again.")

    if attempts == 3:
        print(get_parity_hint(random_number))
    if attempts == 5:
        print(get_divisibility_hint(random_number))
    if attempts == 7:
        print(get_range_hint(random_number))
    if attempts == 10:
        get_thefirst_digit_hint(random_number)

    attempts += 1