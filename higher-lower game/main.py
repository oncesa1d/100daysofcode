from art import logo, vs
from game_data import data
import random


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(user_guess, a_follower, b_followers):
    if a_follower > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
second_account = random.choice(data)


while game_should_continue:

    firs_account = second_account

    if firs_account == second_account:
        second_account = random.choice(data)

    print(f"Compare A: {format_data(firs_account)}")
    print(vs)
    print(f"Against B: {format_data(second_account)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = firs_account["follower_count"]
    b_follower_count = second_account["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You`re right! You`re score now {score}")
    else:
        print(f"Sorry,  that's wrong. You`re final score is  {score}")
        game_should_continue = False
