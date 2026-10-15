# Triangle Type

# Input three sides.

# Print:

# Equilateral (all sides equal)
# Isosceles (two sides equal)
# Scalene (all sides different)

side_a = int(input("Enter the side A of a triangle:"))
side_b = int(input("Enter the side B of a triangle:"))
side_c = int(input("Enter the side C of a triangle:"))

if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
    print("Invalid Triangle! the sum of any two sides must be grater than third side")
elif (side_a == side_b and side_b == side_c and side_a != side_c):
    print("Equilateral (all sides equal)")
elif (side_a != side_b and side_b != side_c):
    print("Scalene (all sides different)")
else:
    print("Isoscles (two sides equal)")
