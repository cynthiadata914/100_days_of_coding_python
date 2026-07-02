#Jungle Adventure
print("Welcome to Jungle Adventure. ")
print("Your mission is to find the Jungle Treasure. ")

point1 = input("You are at a trail. where do you want to go Type 'north' or 'south': ").lower()
if point1 == "north":
    point2 = input("You have reached a river. type 'build raft' or 'swim': ").lower()
    if point2 == "build raft":
        point3 = input("You will find three caves. pick one: 'black', 'gold', or 'white' ").lower()
        if point3 == "gold":
            print("Jungle Treasure found. You win! ")
        elif point3 == "black":
            print("Bat attack. Game over! ")
        elif point3 == "white":
            print("Dead end. Game over! ")
        else:
            print("Wrong choice of cave. Game over!")
    else:
        print("You got eaten by jungle beasts. Game over!")
else:
    print("You got lost in the jungle. Game over!")

