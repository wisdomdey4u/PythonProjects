from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

# Function to check users' guess against actual answer.
def check_answer(user_guess, actual_guess, turns):
    """Checks answer against guess, return the number of turns remaining"""
    if user_guess > actual_guess:
        print("Too high")
        return turns - 1
    elif user_guess < actual_guess:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_guess}")

# Function to set difficulties.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Choose a random number between 1 and 100.
    print("Welcome to the guessing game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"Press, the correct answer is {answer}")


    turns = set_difficulty()

    # Repeat the guessing function if they get it wrong.

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")


game()
