# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero = [i for i in numbers if i <= 0]
print(negative_zero)


# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [num for row in list_of_lists for num in row]
print(flatten)


# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

num = [(i, 1, i, i*i, i**3, i**4, i**5) for i in range (11)]
print(num)


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
output = [
    [country.upper(), country.upper()[:3], city.upper()] 
    for sublist in countries 
    for country, city in sublist
]
print(output)


# Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
output = [{'country': country.upper(), 'city': city.upper() }
          for sublist in countries
          for country, city in sublist]
print(output)


# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
output = [first +' ' + last for conc in names
          for first, last in conc]
print(output)


# Write a lambda function which can solve a slope or y-intercept of linear functions.
# Formulas based on y = mx + b
# Points passed as tuples: p1 = (x1, y1) and p2 = (x2, y2)

get_slope = lambda p1, p2: (p2[1] - p1[1]) / (p2[0] - p1[0])

get_intercept = lambda p1, p2: p1[1] - (get_slope(p1, p2) * p1[0])

# --- Test Case ---
p1 = (2, 5)
p2 = (6, 13)

print("m =", get_slope(p1, p2))      # Outputs: 2.0
print("b =", get_intercept(p1, p2))  # Outputs: 1.0


