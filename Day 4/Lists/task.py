import random
friends = ("Oma", "Cyndy", "Tonia")

print(random.choice(friends))

# or

random_index = random.randint(a=0, b=2)
print(friends[random_index])
