menu = {
    "Burger": 3500,
    "Pizza": 5000,
    "Rice": 2500,
    "Chicken": 2000,
    "Coffee": 1500
}

print("Welcome to Krush Cafe")

total = 0

while True:
    customers_choice = input("What would you like to order?: ").title()

    if customers_choice in menu:
        price = menu[customers_choice]
        total += price
        print(f"{customers_choice} costs ${price}.")
        print(f"The current total: ${total}.")
    else:
        print("Item not on the menu.")

    another_order = input("Would you like to order anything else? (yes/no): ").lower()

    if another_order != "yes":
        break

print(f"\nYour total bill is ${total}.")
print("Thanks for your patronage")


