# Power Calculator
base = int(input("Enter the base:"))
exponent = int(input('Enter the exponent:'))
power = 1
for i in range(1 , exponent +1):
    power = power * base
print(f"Power of base {base} raise to the exponent {exponent} is {power}")