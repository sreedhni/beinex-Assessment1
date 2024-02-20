# 1) write a single program to handle the following arithmetic operations for addition, subtraction, 
# multiplication , division, floor division,modulus and Exponentiation. 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def floor_division(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a // b

def modulus(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

def exponential(a,b):
    return a ** b

    

def arithmetic_operation(operation, a, b):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    elif operation == "%":
        return modulus(a,b)
    elif operation == "**":
        return exponential(a,b)
    elif operation == "//":
        return floor_division(a,b)


    else:
        return "Error: Invalid operation"

try:
    operation = input("Enter the operation (+, -, *, /,//,%,**): ")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    result = arithmetic_operation(operation, a, b)

    print("Result:", result)
except ValueError:
    print("Please enter valid numeric values for the numbers.")

