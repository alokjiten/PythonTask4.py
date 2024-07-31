def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def calculator():
    print("Welcome to the simple calculator!")
    while True:
        num1 = get_number("Enter first number: ")
        operation = get_operation()
        num2 = get_number("Enter second number: ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"The result of {num1} {operation} {num2} = {result}")

        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break
calculator()
