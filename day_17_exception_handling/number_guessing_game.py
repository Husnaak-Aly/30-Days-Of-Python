# Number Guessing Game with Safe Input
# The computer has a secret number. The user has five guesses.
# - Invalid input must not crash the game.
# - Decide whether invalid input consumes an attempt.
# - Give "Too high" or "Too low" hints.
# - End the game when the number is guessed or attempts run out.
def number_guessing_game():
    import random

    secret_number = random.randint(1, 100)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        try:
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)

            if guess < 1 or guess > 100:
                print("Error: Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You've guessed the number!")
                return

            attempts -= 1
            print(f"Attempts left: {attempts}")

        except ValueError:
            print("Error: Please enter a valid integer.")

    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
print(number_guessing_game())