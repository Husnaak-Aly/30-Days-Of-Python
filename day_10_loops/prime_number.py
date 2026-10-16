# Check Prime Number
x = int(input("Enter the number:"))
sq = int(x) ** 0.5

if x <= 1:
    print(f'{x} is not prime')
else:
    is_prime  = True 
    for i in range(2, int(sq) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{x} is a prime number")
    else:
        print(f"{x} is not a prime")



# Print Primes from 1–100
for i in range(1, 101):
    if i <= 1:
        continue
    is_prime = True
    sq = i ** 0.5

    for j in range(2, int(sq) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
print()


# Count Primes in a Range
count = 0
for i in range(1, 51):
    if i <= 1:
        continue
    is_prime = True
    sq = i ** 0.5

    for j in range(2, int(sq) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print("Total prime in range:",count)
