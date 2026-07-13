import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("Welcome to the Number guessing game!")
print("I am thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts. \n")

while attempts < max_attempts:
    guess = int(input("Enter your gues: "))
    attempts += 1

    if guess == secret_number:
        print("\n Congratulations")
        print(f"You guessed the number {secret_number} in {attempts} attempts.")
        break

    elif guess < secret_number:
        print("Too Low")

    else:
        print("Too High")

    print(f"Attempts remaining: {max_attempts} - {attempts}\n")

if attempts == max_attempts and guess != secret_number:
    print("\n Game Over")
    print(f"The correct number was {secret_number}.")