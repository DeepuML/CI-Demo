def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

result1 = add(10, 5)
result2 = subtract(10, 5)
result3 = multiply(10, 5)
result4 = divide(10, 5)

print("Addition: ", result1)
print("Subtraction: ", result2)
print("Multiplication: ", result3)
print("Division: ", result4)