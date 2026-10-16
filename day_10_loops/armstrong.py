# Armstrong Number Check
# Example:
# 153
# Because:
# 1³ + 5³ + 3³ = 153

x = input("Enter the number to check for armstrong number:")
num_length = len(x)
summ = 0
for i in x:
    summ += (int(i)** num_length)

if summ == int(x):
    print(f"Armstrong" )
else:
    print("Not Armstrong")

count = 0
for i in range(1,1001):
    summ = 0
    for j in str(i):
        summ += (int(j)** len(str(i)))
    if summ == i:
        count +=1
print(count)

# pro-tip ----------> can convert int into string once
count = 0
for i in range(1,1001):
    str_num = str(i)
    num_len = len(str_num)
    summ = 0
    for j in str_num:
        summ += (int(j)** num_len)
    if summ == i:
        count +=1
print(count)