# ---------------Level 1-------------------------------

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years

# age = int(input('Enter your age:'))
# if age >= 18:
#     print('You are old enough to learn to drive.')
# else:
#     print(f"you need {18 - age} more years to learn to drive.")



# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
#  You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
# my_age = 21
# your_age = int(input("Enter your age:"))
# if your_age >= my_age:
#     if your_age > my_age:
#         print(f"You are {your_age - my_age} years older than me.")
#     else:
#         print("You and I are the same age.")
# else:
#     print("You are younger than me.")


# Get two numbers from the user using input prompt.
#  If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
# num1 = int(input('Enter the number A:'))
# num2 = int(input("Enter the number B:"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num1 < num2:
#     print(f'{num1} is smaller than {num2}.')
# else:
#     print("both numbers are equal.")


# ---------------------Level 2-----------------------------------------

# Write a code which gives grade to students according to theirs scores:
# score = int(input('Enter your score:'))
# if score >= 90 and score <= 100:
#     print("A grade")
# elif score >= 80 and score < 90:
#     print("B grade")
# elif score >= 70 and score < 80:
#     print("C grade")
# elif score >= 60 and score < 70:
#     print("D grade")
# elif score >= 0:
#     print("F")


# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
# the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# autumn = ["september","october","november"]
# winter = ["december", "january", "febuary"]
# spring = ["march","april", "may"]
# summer = ["june", "july", "august"]

# month = str(input("Enter the name of month:")).lower()
# if month in autumn:
#     print("It is autumn.")
# elif month in winter:
#     print("It is winter.")
# elif month in spring:
#     print("It is spring.")
# elif month in summer:
#     print("It is summer.")
# else:
#     print("Invalid month")


# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# fruit_to_search = str(input("Enter the fruit:")).lower()

# if fruit_to_search not in fruits:
#     fruits.append(fruit_to_search)
#     print("modified list:",fruits)
# else:
#     print("That fruit already exists in the list.")


# --------------------Level 3-------------------------

# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Husnaak',
    'last_name': 'Mansoor',
    'age': 21,
    'country': 'Pakistan',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# middle_skill_index = len(person['skills']) // 2
# if 'skills' in person:
#     middle_skill_index = len(person['skills']) // 2
#     print("middle skill:", person['skills'][middle_skill_index])
# else:
#     print("skills key doesnt exist")


#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# if 'skills' in person:
#     if 'Python' in person['skills']:
#         print('Python')
#     else:
#         print("This skill does not exist")
# else:
#     print("This key does not exist")


#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# frontend = {'JavaScript', 'React'}
# backend = {'Node', 'Python', 'MongoDB'}
# full_stack = {'React', 'Node', 'MongoDB'}
# skills_set = set(person['skills'])
# if 'skills' in person:
#     if full_stack.issubset(skills_set):
#         print('He is a fullstack developer')
#     elif frontend.issubset(skills_set):
#         print('He is a front end developer')
#     elif backend.issubset(skills_set):
#         print('He is a full stack developer')
#     else:
#         print('unknown title')
# else:
#     print('skills key not found in dictionary') -----------> used set because it is orderless and if someone have skills shuffled, it does not throw error


#  * If the person is married and if he lives in Pakistan, print the information in the following format:
#     Asabeneh Yetayeh lives in Pakistan. He is married.
# if person['is_married'] is True:
#     if person['country'] == 'Pakistan':
#         print(f'{person["first_name"]} {person["last_name"]} lives in Pakistan. He is married')
#     else:
#         print('He is married but does not live in Pakistan')
# else:
#     print('He is not married')