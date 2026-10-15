# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# ------------Level 1---------------------------------------

# Find the length of the set it_companies
# print(len(it_companies))


# Add 'Twitter' to it_companies
# it_companies.add('Twitter')
# print(it_companies)


# Insert multiple IT companies at once to the set it_companies
# it_companies.update(['Twitter', 'Meta', 'Tencent'])
# print(it_companies)

# Remove one of the companies from the set it_companies
# it_companies.remove('Facebook')
# print(it_companies)


# What is the difference between remove and discard
# both remove and discard funtion are used to remove an element from the set but if the element is not found remove() throws an error
# while discard doesnt throw the error it element is not found

# --------------Level 2---------------------------------------

# Join A and B
# C = A.union(B)
# C = A | B
# print(C)


# Find A intersection B
# C = A & B
# C = A.intersection(B)
# print(C)


# Is A subset of B
# print(A.issubset(B)) True


# Are A and B disjoint sets
# print(A.isdisjoint(B)) False


# Join A with B and B with A
# print(A | B)
# print(B | A)


# What is the symmetric difference between A and B
# A.symmetric_difference_update(B)
# print(A)


# Delete the sets completely
# del A, B
# print(A) throws error because deleted
# print(B) throws error because deleted


# ---------------------Level 3------------------------------------

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# age_set = set(age)
# print("Length of list:", len(age))
# print("Length of set:",len(age_set))
# print("Length of set is less than List:", len(age) > len(age_set))


# Explain the difference between the following data types: string, list, tuple and set
# Strings are immutable data types used for writing any type of text.
# List is the one of collection datatypes that is ordered and mutable.
# tuple is also the collection datatype that is ordered but immutable( can not add or remove).
# Set os the collection of unordered, unindexed, and immutable elements. doesnt allow duplicate elements. Existing items are immutable 
# but we can add or remove new items

 
# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words 
# Sentence = "I am a teacher and I love to inspire and teach people."
# words = Sentence.split(" ")
# print(words)
# words_set = set(words)
# print("Unique words:", len(words_set))