x = int(input("Enter number:"))
summ = 0
for i in range(1, x):
    if x % i == 0:
        summ += i
if x == summ:
    print("Perfect")
else:
    print("Not perfect")