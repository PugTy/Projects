#Spring 2023 CS1 Project 3 Tyler
# comments: 
# add unit-test for your scenarios 
# you condition @ 32 does not work because it is not a collection (aka list, aka  array), try 
#    if "0123456789".find(digit):   .. instead, or use collection type e.g. digits = ("1", "2", ...)

import random

def generate_code():
    digits = "0123456789"
    code = ""
    while len(code) < 4:
        digit = random.choice(digits)
        if digit not in code:
            code += digit
    return code

def score_guess(guess, secret_num):
    correct_position = 0
    correct_digit = 0
    for i in range(4):
        if guess[i] == secret_num[i]:
            correct_position += 2
        elif guess[i] in secret_num:
            correct_digit += 1
    return correct_position + correct_digit

def valid_guess(guess):
    if guess == "quit":
        return True
    if len(guess) != 4:
        return False
    for digit in guess:
        if digit not in "0123456789":
            return False
        if guess.count(digit) > 1:
            return False
    return True

def play_game():
    print("Welcome to Guess the Code!")
    secret_num = generate_code()
    num_guesses = 0
    while True:
        guess = input("What is your guess? ")
        if guess == "quit":
            print("The secret code was", secret_num)
            print("You made", num_guesses, "guesses. Goodbye!")
            return
        if not valid_guess(guess):
            print("Invalid input. Your guess must be either 4 different digits or 'quit'.")
            continue
        num_guesses += 1
        score = score_guess(guess, secret_num)
        if score == 8:
            print("Congrats! You guessed the number in", num_guesses, "guesses!")
            return
        else:
            print("Your guess scored", score)

play_game()
