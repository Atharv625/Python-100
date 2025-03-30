# calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def calculator(a):
    match(a):
        case 1:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Result: {add(x, y)}")
        case 2:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Result: {subtract(x, y)}")
        case 3:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Result: {multiply(x, y)}")
        case 4:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Result: {divide(x, y)}")
        case _:
            print("Invalid operation")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = int(input("Enter operation (1/2/3/4): "))
calculator(operation)
