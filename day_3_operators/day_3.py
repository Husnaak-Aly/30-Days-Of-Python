import math
age = 21
height = 180.0
a = 1 + 1j

# Area of Triangle
base = int(input('Enter the base:'))
height = int(input('Enter the height:'))
area_of_triangle = 0.5 * base * height
print('Area of triangle:', area_of_triangle)


# Perimter of Triangle
side_a = int(input('Enter Side A:'))
side_b = int(input('Enter Side B:'))
side_c = int(input('Enter Side C:'))
Perimeter = side_a + side_b + side_c
print('Perimeter of triangle:', Perimeter, 'meters')


# Area and Perimeter of Rectangle
length = int(input('Enter the length:'))
width = int(input('Enter the width:'))
Area_of_rectangle = length * width
perim = 2*(length + width)
print('Area of Rectangle:',Area_of_rectangle,'m^2')
print('Perimter of Rectangle:',perim,'meters')


# Area of a circle
radius = int(input('Enter the radius:'))
pi_ = 3.142
area_of_circle = pi_*radius*radius
print('Area of Circle:', area_of_circle, 'm^2')


# Slope, x-intercept, y-intercept of y=2x-2
# Standard equation => y=mx+b, where m= slope and b = y-intercept
m = 2
b = -2
slope = m
y_intercept = (0 , b) # where x = 0
x_intercept = (-b/m , 0)
print('Slope:',slope)
print('y-intercept:',y_intercept)
print('x-intercept:', x_intercept)


# slope and euclidean distance(ed)
x1, y1 = 2,2
x2, y2 = 6,10
slope2 = (y2-y1)/(x2-x1)
print('Slope:',slope2)
ed = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print(ed)


# compare both slopes
print(slope == slope2)


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x= int(input('Enter value of x:'))
y= (x**2) + 6*x + 9
print('y = ',y) 


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python'))
print(len('dragon'))
print(len('python') != len('dragon'))


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in "I hope this course in not full of jargon")


# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')


# # Find the length of the text python and convert the value to float and convert it to string
lenth = len('python')
print(float(lenth))
print(str(lenth))


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Enter number:'))
rem = num % 2
check = 0
print('Even:', rem == check)


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
fd = 7 // 3
cv = int(2.7)
print(fd == cv)


# Check if type of '10' is equal to type of 10
print(type('10') == type(10))


# Check if int('9.8') is equal to 10
print(int(9.8) == 10)


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours:'))
rate_per_hour = int(input('Enter rate per hour:'))
pay = hours * rate_per_hour
print(pay)


# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
seconds_in_year = 31536000
years = int(input('Enter number of years you have lived:'))
total_sec = seconds_in_year * years
print('you have lived for',total_sec,'seconds')


print('10' is 10)