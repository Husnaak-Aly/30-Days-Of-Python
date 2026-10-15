num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
op = input("Enter the operator (+, - *, /, **, //)").strip(" ")

match op:
    case "+":
        print("Sum of the numbers is", num1 + num2)
    case "-":
        print("Difference of two numbers is", num1 - num2)
    case "*":
        print("Product of both numbers is",num1 * num2)
    case "/" if num2 != 0:
        print("num1 divided by num2 is", num1 / num2)
    case "/" if num2 == 0:
        print("Can not divide by zero!")
    case "**" if (num1 == 0 and num2 < 0):
        print("Can not rise zero to the negative power")
    case "**":
        print("Num1 raise to the power num2 is", num1 ** num2)
    case "//" if num2 != 0:
        print("Floor division of both is", num1 // num2)
    case "//" if num2 == 0:
        print("Can not divide by zero")
    case _:
        print("Invalid operator!")
