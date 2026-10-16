# --------------Level 1----------------------

# Iterate 0 to 10 using for loop, do the same using while loop

num = 0
while num < 11:
    print(num)
    num += 1

for i in range(11):
    print(i)


# Iterate 10 to 0 using for loop, do the same using while loop.

num = 10
while num > 0:
    print(num)
    num -= 1

for i in range(10,0,-1):
    print(i)


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######

for i in range(1,8):
   print("*" * i)


# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for k in range(8):
        print("#", end="")
    print()


for i in range(1, 9):
        print("#"*8)

i = 0
while i < 8:
    print("#"* 8)
    i+=1


# Print the following pattern
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range (11):
    print(f"{i} x {i} = {i*i}")
i = 0
while i < 11:
    print(f"{i} x {i} = {i*i}")
    i+=1



# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python','Numpy','Pandas','Django','Flask']
for i in lst:
    print(i)


# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range (0,101,2):
    print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,101):
    if i % 2 != 0:
        print(i)
    

# -----------------------Level 2--------------------------------

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
temp = 0
for i in range(0,101):
    temp += i
print("The sum of all numbers is",temp)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
temp_even = 0
temp_odd = 0
for i in range(101):
    if i % 2 == 0:
        temp_even += i
    else:
        temp_odd += i
print(f"Sum of even numbers is {temp_even}. Sum of odd numbers is {temp_odd}.")


# ---------------------------Level 3----------------------------------

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
i = len(fruits)
for j in range(i-1, -1, -1):
    print(fruits[j])

for fruit in reversed(fruits):
    print(fruit)





