num_to_check = int(input("What number would you like to check? "))
if (num_to_check % 2) == 0:
    print("Even")
    age = int(input("What is your age? " ))
    if age <= 18:
        print("Please pay $7. ")
    else:
        print("Please pay $12. ")
else:
    print("Odd")

