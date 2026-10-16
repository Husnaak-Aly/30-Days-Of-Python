# Count Positive Numbers
# Ask the user for 5 numbers.
# Count how many are positive.

i = 1
pos = 0

while i < 6:
    x = int(input(f"Enter number {i}:"))
    if x > 0:
        pos += 1
    i += 1 
print("Total positive numbers are", pos)
pos = 0
for i in range(5):
    x = int(input("enter number:"))
    if x > 0:
        pos += 1
print(pos)



# Count Even and Odd
# Ask the user for 10 numbers.
even = 0
odd = 0
for i in range(10):
    x = int(input(f"Enter the number {i +1}:"))
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even count:",even)
print("Odd count:",odd)



# Largest Number
# Take 5 numbers and find the largest.
p = 0
for i in range(5):
    x = int(input(f"Enter number {i +1}:"))
    if x > p:
        p = x
print("Largest number:", p)


# Smallest Number
# Take 5 numbers and find the smallest.
small = None
for i in range(5):
    x = int(input(f"Enter the number {i+1}:"))
    if small is None or x < small:
        small = x
print("small:",small)


# Average Calculator
# Take 5 numbers and calculate the average.
sum = 0
count = 0
for i in range(5):
    x = int(input(f"Enter the number {i+1}:"))
    sum += x
    count += 1
print(f"Average: {sum/count:.2f}")
