#Restaurant name generator
import random

foods = ["Burger", "Pizza", "Chicken", "Pasta", "Grill"]
adjectives = ["Golden", "Royal", "Urban", "Fresh", "Happy"]
endings = ["Kitchen", "Spot", "House", "Corner", "Place"]

print("Welcome to Restaurant Name Generator!")
r_foods = int(input("How many foods do you like? "))
r_adjectives = int(input("What adjective suits the food name? "))
r_endings = int(input("Which ending compliments your answer? "))

restaurant_name = []
for food in range(0, r_foods):
    restaurant_name.append(random.choice(foods))
for adjective in range(0, r_adjectives):
    restaurant_name.append(random.choice(adjectives))
for ending in range(0, r_endings):
    restaurant_name.append(random.choice(endings))

print(restaurant_name)
random.shuffle(restaurant_name)
print(restaurant_name)

restaurant_chosen_name = ""
for name in restaurant_name:
    restaurant_chosen_name += name

print(f"Your Restaurant Name is: {restaurant_chosen_name}")
