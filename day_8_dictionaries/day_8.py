# Create an empty dictionary called dog
dog = {}


# Add name, color, breed, legs, age to the dog dictionary
dog = {'name' : 'Pluto', 'color' : 'brown', 'legs' : 4, 'age' : ' 5'}


# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Husnaak',
    'last_name' : 'Mansoor',
    'gender' : 'male',
    'age' : 21,
    'marital_status' : 'single',
    'skills' : ['Java', 'Python', 'C++', 'SQL'],
    'country' : 'Pakistan',
    'city' : 'Hyderabad',
    'address' : {
        'street' : 'Allahwala',
        'zipcode' : '1324'
    }
}


# Get the length of the student dictionary
print(len(student))


# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))


# Modify the skills values by adding one or two skills
student['skills'] += ['AI', 'Javascript']
print(student['skills'])


# Get the dictionary keys as a list
print(student.keys())


# Get the dictionary values as a list
print(student.values())


# Change the dictionary to a list of tuples using items() method
x = student.items()
print(x)


# Delete one of the items in the dictionary
student.pop('first_name')
print(student)


# Delete one of the dictionaries
del dog
print(dog)