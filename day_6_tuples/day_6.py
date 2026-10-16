# ---------------LEVEL 1-------------------------------

# Create an empty tuple
new_tuple = tuple()


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Yousif', 'Amjad', 'Jamal')
sisters = ('Rozy', 'Hania', 'Marvi')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)


# How many siblings do you have?
print('How many siblings do I have?', len(siblings))


# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('Jack')
siblings.append('Jill')
siblings[0:0] = ['Jack', 'Jill']
siblings.extend(['Jack', 'Jill'])
siblings += ['Jack', 'Jill']
family_members = tuple(siblings)
print(family_members)

# --------------------LEVEL 2-------------------------------

# Unpack siblings and parents from family_members
siblings1 = family_members[0:6]
print(siblings1)
parents = family_members[-2:]
print(parents)


# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('mango', 'banana', 'lemon')
vegetables = ('potato', 'cauliflower', 'tomato')
animal_products = ('mutton', 'beef', 'bacon')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)


# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = len(food_stuff_lt) // 2
print('Middle item:', food_stuff_lt[middle_item])


# Slice out the first three items and the last three items from food_stuff_lt list
print("First three items are:",food_stuff_lt[0:3])
print("Last three items are:",food_stuff_lt[-3:])


# Delete the food_stuff_tp tuple completely
del food_stuff_tp


# Check if an item exists in tuple:
print('beef' in food_stuff_tp)


# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)


# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

