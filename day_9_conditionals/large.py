# Largest of Two Numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > num2:
    print("1st number is greater than 2nd number")
elif num2 > num1:
    print("2nd number is greater than 1st number")
else:
    print("both are equal")



# Largest of 3 number 
a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))
c = int(input("Enter the number c:"))

if (a >= b and a >= c):
    print("a is the largest number")
elif b >= c:
    print("b is the largest number")
else:
    print("c is the largest number")