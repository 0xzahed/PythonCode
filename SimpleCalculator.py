def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

while True:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    operation = input("Enter operation (+, -, *, /) or 'exit' to end: ")

    if operation.lower() == 'exit':
        print("Calculator exiting. Goodbye!")
        break

    if operation == '+':
        result = add(x, y)
    elif operation == '-':
        result = subtract(x, y)
    elif operation == '*':
        result = multiply(x, y)
    elif operation == '/':
        result = divide(x, y)
    else:
        result = "Invalid operation entered."

    print(f"Result: {result}\n")
