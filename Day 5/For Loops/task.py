#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
    #print(fruit)
    #print(fruit + " pie")

# Todo 1 print numbers from(1-20)
for numbers in range(1, 21):
    print(numbers)

# Todo 2 print out the even numbers within(1-50)
for numbers in range(1, 51, 2):
    print(numbers)

# Todo 3 sum of numbers(1-100)
total = 0
for numbers in range(1, 101):
    total += numbers
    print("The sum is", total)

# Todo Multiplication table
number = int(input("Enter a number: "))
for n in range(1, 13):
    print(f"{number} * {n} = {number * n}")

# Todo count vowels
text = input("Enter a sentence: ")
count =0
for letter in text.lower():
    if letter in "aeiou":
        count += 1
print("Number of vowels:", count)

# Todo reverse a string
word = input("Enter a word: ")
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word
print("Reversed word:", reversed_word)

# Todo find the largest number
numbers = [23, 27, 64, 33, 56]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest number:", largest)

# Todo Count positive numbers
numbers = [-4, 3, -9, 10, 4, -5]
count = 0
for number in numbers:
    if number >0:
        count += 1
print("Positive numbers:", count)

# Todo print a star pattern
for a in range(1,6):
    print("*" * a)

# Todo Fizz buzz
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

