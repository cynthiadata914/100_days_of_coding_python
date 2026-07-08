import art
def add(n1, n2):
    return n1 + n2

# Todo 1 write out other 3 functions - subtract,multiply and divide
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Todo 2 add these 4 functions into a dictionary as the values. keys = +, -, *, /.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Todo 3 use the dictionary operations to perform the calculations.multiply 4*8
# Check if the user wants to continue using the previous result.
def calculator():
    print(art.logo)
    next_decision = True
    num_one = float(input("What is the first number?: "))


    while next_decision:
        for symbol in operations:
            print(symbol)
        operation_choice = input("Select an operation: ")
        num_two = float(input("What is the second number?: "))
        result = operations[operation_choice](num_one, num_two)
        print(f"{result}")

        decision = input(f"Type 'y' to continue with {result} or 'n' to start a new calculation:")

        if decision == "y":
            num_one = result
        else:
            next_decision = False
            print("\n" * 20)
            calculator()

calculator()
