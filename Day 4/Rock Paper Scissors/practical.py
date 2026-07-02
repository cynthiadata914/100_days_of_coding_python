import random
animal_names = ["Lion", "Snake", "Eagle"]

user_pick = int(input("What do you choose? Type 0 for Lion, 1 for Snake, 2 for Eagle: "))
if user_pick >= 0 and user_pick <= 2:
    print(animal_names[user_pick])

computer_pick = random.randint(0, 2)
print("Computer picked: ")
print(animal_names[computer_pick])

if user_pick >= 3 or user_pick < 0:
    print("Out of range. You loose!")
elif user_pick == 0 and computer_pick == 2:
    print("user won! computer lost!")
elif computer_pick == 0 and user_pick == 2:
    print("computer won! user lost!")
elif computer_pick > user_pick:
    print("computer lost! user won!")
elif user_pick > computer_pick:
    print("computer won! user lost!")
else:
    print("It is a draw!")
