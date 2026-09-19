def square(number):
    return number * number

def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

number = float(input("Enter a number to find its square: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print("Square:", square(number))
print("Average:", average(num1, num2, num3))