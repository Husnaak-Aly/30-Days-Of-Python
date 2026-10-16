# Declare an empty list
lst = []


# Declare a list with more than 5 items
lst = ['mango', 'orange', 'apple', 'banana', 'chikoo']

# Find the length of your list
print(len(lst))


# Get the first item, the middle item and the last item of the list
last_item = len(lst) - 1
print('First item:',lst[0])
print('Last item:',lst[last_item])
middle_index = len(lst) // 2
print('Middle item:',lst[middle_index])


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Husnaak", 21, 18.0, False, "Wadhu Wah, Hyderabad"]


# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)


# Print the number of companies in the list
num_of_it_companies = len(it_companies)
print('Number of IT companies:',num_of_it_companies)


# Print the first, middle and last company
print('First Company in list:',it_companies[0])
last_comp = num_of_it_companies - 1
print('Last Company:',it_companies[last_comp])
middle_comp = num_of_it_companies // 2
print('Middle Company',it_companies[middle_comp])


# Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)


# Add an IT company to it_companies
it_companies.append('Netflix')
print(it_companies)


# Insert an IT company in the middle of the companies list
middle_of_companies = len(it_companies) // 2
it_companies[middle_of_companies] = 'X'
print(it_companies)


# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] =it_companies[0].upper()
print(it_companies)


# Join the it_companies with a string '#;  '
result = '#; '.join(it_companies)
print(result)


# Check if a certain company exists in the it_companies list.
does_Exist = 'Facebook' in it_companies
print('Does this IT company exist:',does_Exist)


# Sort the list using sort() method
it_companies.sort()
print(it_companies)


# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)


# Slice out the first 3 companies from the list
print(it_companies[0:3])


# Slice out the last 3 companies from the list
print(it_companies[-3:])
print(it_companies[-1:-3])


# Slice out the middle IT company or companies from the list
middle = len(it_companies) // 2
print(it_companies[middle])


# For even list, find middle
lst = ['HM', 'MY', 'AC', 'ZB']
right_mid = len(lst) // 2
left_mid = (len(lst) // 2) - 1
print(lst[left_mid],lst[right_mid])


# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)


# Remove the middle IT company or companies from the list
mid = len(it_companies) // 2
it_companies.pop(mid)
print(it_companies)


# Remove the last IT company from the list
last_comp = len(it_companies) - 1
it_companies.pop(last_comp)
print(it_companies)


# Remove all IT companies from the list
it_companies.clear()
print(it_companies)


# Remove all IT companies from the list
del it_companies
print(it_companies)


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
result = front_end + back_end
print(result)
front_end.extend(back_end)
print(front_end)


# Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = result.copy()
redux_place = len(front_end) - 1
full_stack.insert(redux_place+1,'Python')
full_stack.insert(redux_place+1,'SQL')
print(full_stack)



# -----------------LEVEL 2------------------

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print('min:',max(ages))
print('min:',min(ages))


# Add the min age and the max age again to the list
min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)
print(ages)


# Find the median age (one middle item or two middle items divided by two)
ages.sort()
right_mid = len(ages) // 2
left_mid = right_mid - 1
median = (ages[right_mid] + ages[left_mid]) / 2
print(median)


# Find the average age (sum of all items divided by their number )
# ages.sort
avg = sum(ages) / len(ages)
print(avg)


# Find the range of the ages (max minus min)
# ages.sort
min_age = min(ages)
max_age = max(ages)
rangee = max_age - min_age
print(rangee)


# Compare the value of (min - average) and (max - average), use abs() method
compare = abs(min_age - avg) is abs(max_age - avg)
print(compare)