from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5
print(logo)


def find_answer(user_guess, actual_answer, attempts):
    if user_guess > actual_answer:
        print("Too high")
        return attempts - 1
    elif user_guess < actual_answer:
        print("Too low")
        return attempts - 1

    else:
        print(f"You got it! The answer was {actual_answer}")


def hard_or_easy():
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    print(f"The number is {number}")

    attempts = hard_or_easy()

    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = find_answer(guess, number, attempts)
        if attempts == 0:
            print("You lose!")
            return
        elif guess != number:
            print("Guess again. ")
game()
