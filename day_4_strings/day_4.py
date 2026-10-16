# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
s1 = 'Thirty '
s2 = 'Days '
s3 = 'Of '
s4 = 'Python'
constr = s1 + s2 + s3 + s4
print(constr)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
s5 = 'Coding'
s6 = 'For'
s7 = 'All'
concstr = s5 + ' ' + s6 + ' ' +  s7
print(concstr)
# also
word = ['coding','for','all']
sentence = " ".join(word)
print(sentence)


# Declare a variable named company and assign it to an initial value "Coding For All". and also print
company = "Coding For All"
print(company)

# Print the length of the company string using len() method and print().
print(len(company))


# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())


# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())


# Cut(slice) out the first word of Coding For All string.
new_str = company[0:6]
print(new_str)


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('coding'))
print(company.index('coding'))


# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('coding','python'))


# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
company2 = 'Python for Everyone'
print(company2.replace('Python for Everyone','Python for All'))


# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))


# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
strr = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(strr.split(', '))


# What is the character at index 0 in the string Coding For All.
print(company[0])


# # What is the last index of the string Coding For All.
last_index = len(company) - 1
print(last_index)
print(company[13])


# What character is at index 10 in "Coding For All" string.
print(company[10])


# Create an acronym or an abbreviation for the name 'Python For Everyone'.
strr = 'Python For Everyone'
a,b,c = strr.split(' ')
abr = a[0] + b[0] + c[0]
print(abr)
sentence = 'Python For Everyone Extra words here'
a,b,c, *extra = sentence.split(' ')
abr = a[0] + b[0] + c[0]
print(abr)


# Create an acronym or an abbreviation for the name 'Coding For All'.
a,b,c = company.split(' ')
abr = a[0]+b[0]+c[0]
print(abr) 


# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))


# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))


# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))


# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
#  'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
# last occurence
print(sentence.rfind('because'))


# Slice out the phrase 'because because because' in the following sentence:
#  'You cannot end a sentence with because because because is a conjunction'
# 31 54
start = sentence.find('because because because')
end = start + len('because because because')
print(sentence[start:end])


# Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))


# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_str = '   Coding For All      '
print(new_str.strip(' '))


# Which one of the following variables return True when we use the method isidentifier():
s1 = '30DaysOfPython'
s2 = 'thirty_days_of_python'
print(s1.isidentifier()) # false
print(s2.isidentifier()) # true


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
# Join the list with a hash with space string.
py_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(py_lib)
print(result)


# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
sent = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sent)


# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity'.expandtabs(12))
print('Husnaak\t21\tPakistan\tHyderabad'.expandtabs(12))


# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))


# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')