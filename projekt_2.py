"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Daniel Šadibol
email: sadibol.daniel@gmail.com
discord: dzonsnou. 512617534952833034
"""
import random
import time

def generate_secret_number():
    digits = list(range(1, 10))
    random.shuffle(digits)
    secret_number = digits[:4]
    return ''.join(map(str, secret_number))

def validate_guess(guess):
    if len(guess) != 4:
        return False, "Number must be exactly 4 digits long."
    if not guess.isdigit():
        return False, "Number must contain only digits."
    if guess[0] == '0':
        return False, "Number must not start with 0."
    if len(set(guess)) != 4:
        return False, "Number must not contain duplicate digits."
    return True, ""

def evaluate_guess(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def bulls_and_cows_game():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ")
        is_valid, message = validate_guess(guess)
        if not is_valid:
            print(message)
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        if bulls == 1:
            bull_word = "bull"
        else:
            bull_word = "bulls"

        if cows == 1:
            cow_word = "cow"
        else:
            cow_word = "cows"

        print(f"{bulls} {bull_word}, {cows} {cow_word}")

        if bulls == 4:
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"It took you {time_taken:.2f} seconds.")
            break

if __name__ == "__main__":
    bulls_and_cows_game()
