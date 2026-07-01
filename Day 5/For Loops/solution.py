#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
#    print(fruit)
#    print(fruit + " pie")

#print(fruits)

# Todo password checker
password = ""
while password != "python987":
    password = input("Enter password: ")
print("Access Granted")

# Todo guess the secret number
secret_number = 23
guess = 0
while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess != secret_number:
        print("Try again")
print("Congratulations! you guessed correctly.")

# Todo countdown timer
count = int(input("Enter a starting number: "))
while count > 0:
    print(count)
    count -= 1
print("Blast Off!")

# Todo sum until zero
total = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))
print("Total =", total)

# Todo Atm menu
balance = 1000
choice = 0
while choice != 4:
    print("n\1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful.")
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    elif choice == 4:
        print("Thank you for using our ATM!")
    else:
        print("Invalid choice.")
