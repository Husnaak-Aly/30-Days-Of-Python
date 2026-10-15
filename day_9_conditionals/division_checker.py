# Take a number and check:

# Divisible by both 3 and 5
# Divisible only by 3
# Divisible only by 5
# Divisible by neither

num = int(input("Enter the number:"))
if (num % 3 == 0 and num % 5 == 0):
    print("Divisible by both 3 and 5")
elif num % 3 == 0 :
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Divisible by neither")
    