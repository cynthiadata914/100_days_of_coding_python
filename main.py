# Display art
from art import logo, vs
from game_data import data
import random

def format_data(accts):
    """Takes the account data and returns a printable format."""
    acct_name = accts["name"]
    acct_descr = acct_a["description"]
    acct_country = acct_a["country"]
    return f"{acct_name}, a {acct_descr}, from{acct_country}"

# - Use if statement to check if user is correct.
def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and followers counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True

 # Generate a random account for the game data
acct_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Making account at position B become the next account at position A.
    acct_a = acct_b
    acct_b = random.choice(data)

    if acct_a == acct_b:
        acct_b = random.choice(data)

    print(f"Compare A: {format_data(acct_a)}.")
    print(vs)
    print(f"Against B: {format_data(acct_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)

    # Check if user is correct.
    # - Get follower count of each account
    a_follower_count = acct_a["follower_count"]
    b_follower_count = acct_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that is wrong. Final score: {score}.")
        game_should_continue = False

