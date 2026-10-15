#  -------------------------LEVEL 1-----------------------------------

# Declare a function add_two_numbers. It takes two parameters and it returns a sum
# def add_two_numbers(n1, n2):
#     return n1 + n2
# print(add_two_numbers(3,4))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle (radius):
#     PI = 3.14
#     return(PI *radius *radius)
# x = int(input("enter the radius of circle to get the area:"))
# print(area_of_circle(x))


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
# def add_all_nums(*args):
#     for num in args:
#         print(type(num))
#     return sum(args)
# print(add_all_nums(3,4,5))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# def convert_celsius_to_fahrenheit (celcius):
#     Fahrenheit = (celcius * 9/5) + 32
#     return Fahrenheit
# print(convert_celsius_to_fahrenheit(-41))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def check_season(month):
#     if month in ["march", "april", "may"]:
#         print("Spring")
#     elif month in ["june", "july", "august"]:
#         print("Summer")
#     elif month in ["september", "october", "november"]:
#         print("Autumn")
#     elif month in ["december", "january", "february"]:
#         print("Winter")
#     else:
#         print("Invalid Input")

# check_season(input("Enter the name of month to know the season:").strip().lower())

# def check_season_pro(month):
#     # Map months to their seasons
#     seasons = {
#         "march": "Spring", "april": "Spring", "may": "Spring",
#         "june": "Summer", "july": "Summer", "august": "Summer",
#         "september": "Autumn", "october": "Autumn", "november": "Autumn",
#         "december": "Winter", "january": "Winter", "february": "Winter"
#     }

#     # Use .get() to look up the month. If it doesn't exist, return "Invalid Input"
#     print(seasons.get(month, "Invalid Input"))

# check_season_pro(input("Enter the name of month: ").strip().lower())


# Write a function called calculate_slope which return the slope of a linear equation
# def calculate_slope(x1,y1,x2,y2):
#     return (y2 - y1) / (x2 - x1)
# print(calculate_slope(2,4,5,2))


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# def solve_quadratic_eqn(a, b, c):
#     discriminant = (b*b - (4*a*c))**0.5
#     r1 = (-b + discriminant) / (2*a)
#     r2 = (-b - discriminant) / (2*a)
#     return r1, r2
# print(solve_quadratic_eqn(-1, 2, 3))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(list_):
#     for i in list_:
#         print(i)
# l1 = [1,2,3,4,52,5]
# print_list(l1)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# def reverse_list(arr):
#     for i in reversed(arr):
#         print(i)
# array = (1,2,3,4)
# reverse_list(array)

# def reverse_list(arr):
#     output = []
#     for i in reversed(arr):
#         output.append(i)
#     return output
# array = [1,2,3,4,5]
# print(reverse_list(array))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(lst):
#     output = []
#     for i in lst:
#         output.append(str(i).capitalize())
#     return output
# print(capitalize_list_items(['ali','amju']))
# # ------->Pro-tip----Use list-comprehension
# def capitalize_list_items(lst):
#     # This single line replaces your empty list, your for loop, and your append step!
#     return [str(i).capitalize() for i in lst]

# print(capitalize_list_items(['ali', 'amju']))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end
# def add_item (lst, item):
#     output= []
#     for i in lst:
#         output.append(i)
#     output.append(item)
#     return output
# food= ['apple','mango','banana']
# print(add_item(food, 'kiwi'))
# ------------>pr-tip use copy function
# def add_item(lst, item):
#     output = lst.copy()
#     output.append(item)
#     return output
# food= ['apple','mango','banana']
# print(add_item(food, 'kiwi'))



# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# def remove_item(lst, item):
#     output = lst.copy()
#     output.remove(item)
#     return output
# num = [1,2,3,4,5]
# print(remove_item(num,3))


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# def sum_of_numbers(num):
#     sum_num = 0
#     for i in range(num+1):
#         sum_num += i
#     return sum_num
# print(sum_of_numbers(100))


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds(num):
#     sum_odd = 0
#     for i in range(num+1):
#         if i % 2 != 0:
#             sum_odd += i
#     return sum_odd
# print(sum_of_odds(10))


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_even(num):
#     sum_even = 0
#     for i in range(num+1):
#         if i % 2 == 0:
#             sum_even += i
#     return sum_even
# print(sum_of_even(10))


# ----------------------LEVEL 2--------------------------

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the numbeder.
# def even_and_odds(num):
#     count_even = 0
#     count_odd = 0
#     for i in range(num + 1):
#         if i % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     return count_even, count_odd
# print(even_and_odds(10)) 


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     if num > 1:
#         return num * factorial(num - 1)
#     return "negatives do not have factorials"
# print(factorial(-1))

    
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# def is_empty(para):
#     return len(para) == 0
# lst = []
# print("Empty:",is_empty(lst))


# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# def calculate_mean(lst):
#     return sum(lst) / len(lst)

# def calculate_median(lst):
#     sorted_lst = sorted(lst)
#     mid_index = len(sorted_lst) // 2
#     if len(lst) % 2 != 0:
#         return sorted_lst[mid_index]
#     else:
#         left_mid = sorted_lst[mid_index - 1]
#         right_mid = sorted_lst[mid_index]
#         return (left_mid + right_mid) / 2
# print(calculate_median([1,2,3]))
# print(calculate_median([1,2,3,4]))

# def calculate_range(lst):
#     lst_copy = sorted(lst.copy())
#     high = lst_copy[-1]
#     low = lst_copy[0]
#     range_ = high - low
#     return range_
# print(calculate_range([1,2,3,4,5]))
# ------------------->Pro-way
# def calculate_range(lst):
#     return max(lst) - min(lst)
# print(calculate_range([1,2,3,4,5]))


# Write a function called greet which takes a default argument, name. 
# If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
# def greet(name = 'Guest!'):
#     print('Hello,', name)
# greet("Husnaak")

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values
# def show_args(**kwargs):
#     for k ,v in kwargs.items():
#         print("Received: name:", k, "\tvalue:",v)
# show_args(name = "Husnaak", age = 21, city = 'Hyd')



# -------------Level 3---------------------------------

# Write a function called is_prime, which checks if a number is prime.
# def is_prime(num):
#     sq_root = int(num ** 0.5)
   
#     if num < 2:
#         return False
#     for i in range(2,sq_root+1):
#         if num % i == 0 :
#             return False
#     return True
# print(is_prime(53))



# Write a functions which checks if all items are unique in the list.
# def check_unique(lst):
#     lst_copy = lst.copy()
#     for i in lst:
#         lst_copy.remove(i)
#         if i in lst_copy:
#             return False
#     return True
# print(check_unique([1,2,3,1]))
# ----->pro-tip, upper code is slow, gives o(n^2).... better turn list to sets
# def check_unique(lst):
#     return len(lst) == len(set(lst))
# print(check_unique([1,2,3,4]))


# Write a function which checks if all the items of the list are of the same data type.
# def check_same_data_type(lst):
#     if len(lst) == 0:
#         return True
#     new_lst = []
#     new_lst.append(lst[0])
#     for i in lst[1:]:
#         if type(i) == type(new_lst[0]):
#             new_lst.append(i)
#     return lst == new_lst
# print(check_same_data_type(['ali','amju',1]))
# -----------> more mature version
# def check(lst):
#     if not lst: return True
#     for i in lst:
#         if type(i) != type(lst[0]):
#             return False
#     return True
# print(check(['ali','amju',1]))


# Write a function which check if provided variable is a valid python variable
def valid_variable(var):
    return var.isidentifier()
print(valid_variable('_ali'))