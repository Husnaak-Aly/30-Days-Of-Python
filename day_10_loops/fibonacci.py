# print first N fibbonaci numbers

x = int(input("Enter the number:"))
n1 = 0
n2 = 1
for i in range (x):
    print(n1,end=" ")

    nth = n1 + n2

    n1 = n2
    n2 = nth
print()
    
    