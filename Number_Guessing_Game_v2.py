from art import logo
from random import randint
# Generate random number
answer = randint(1, 100)

# Check the numbers
def check_answer(guess, answer, rounds):
    if guess > answer:
        print("Too high.")
        return rounds -1
    elif guess < answer:
        print("Too low.")
        return rounds -1
    else:
        print(f"Bingo! The answer is {answer}.")

EASY_LEVEL_ROUNDS = 10
HARD_LEVEL_ROUNDS = 5

# Set difficulty
def set_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level.lower() == "hard":
        return HARD_LEVEL_ROUNDS
    else:
        return EASY_LEVEL_ROUNDS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {answer}")

    rounds = set_level()
    
    guess = 0
    while guess != answer:
        print(f"You have {rounds} attempts remaining to guess the number.")
        guess = int(input("Make a guess (integer):"))
        rounds = check_answer(guess, answer, rounds)
        if rounds == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()