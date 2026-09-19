num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /, %): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero is not allowed"
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Modulus by zero is not allowed"
else:
    result = "Invalid operation"

print("Result:", result)