# Day 2: 30 days of Python programming
import math

first_name = "Husnaak"
last_name = "Mansoor"
full_name = "Husnaak Mansoor"
country = "Pakistan"
city = "Hyderabad"
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = False
caste, university, district, year_of_admission = "Chandio", "Mehran", "Kamber", 2023

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(caste))
print(type(university))
print(type(district))
print(type(year_of_admission))

print(len(first_name))
print(len(last_name))

print(len(first_name) == len(last_name))

#Calc
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
print(exp)
print(num_one // num_two)

#Area of circle
radius = 30 #meters
pi = 3.142
area_of_circle = pi * (radius **2)
print(area_of_circle, "meters")

#circumference_of_circle 
circumference_of_circle = 2*pi*radius
print(circumference_of_circle)

#radius as input
radius = float(input("Enter the radius:"))
print("area = ", math.pi*radius*radius, "meters")


#bio_data
first_name = input("Enter your first name:")
print(first_name)
last_name = input("Enter your last name:")
print(last_name)
country = input("Enter country name:")
print(country)
age = input("enter the age:")
print(age)

person_info = {'Name':'Husnaak Mansoor',
               'Caste':'Chandio',
               'Country':'Pakistan'}
print(person_info)