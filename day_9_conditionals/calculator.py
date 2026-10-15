# Take:

# First number
# Operator (+, -, *, /)
# Second number

# Perform the operation and print the result
num1 = int(input("Enter the first number:"))
op = input("Enter the operator(+, -, *, /, **, //):")
num2 = int(input("Enter the second number:"))

if op == "+":
    print(f"Sum of the number {num1} and {num2} is {num1 + num2}")
elif op == "-":
    print(f"Difference between number {num1} and {num2} is {num1 - num2}")
elif op == "*":
    print(f"Product of {num1} and {num2} is {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("Can not divide by zero!")
    else:
        print(f"{num1} divided by {num2} gives {num1 / num2:.2f}")
elif op == "**":
    if num1 == 0 and num2 < 0:
        print("can not raise zero to the negative power!")
    else:
        print(f"{num1} to the power {num2} is {num1 ** num2}")
elif op == "//":
    if num2 == 0:
        print("Can not divide by zero!")
    else:
        print(f"floor division of {num1} by {num2} is {num1 // num2}")
else:
    print("Unknown operator")
