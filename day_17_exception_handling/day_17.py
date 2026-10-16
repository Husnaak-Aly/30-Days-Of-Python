#1. Ask the user to enter an integer. If they enter something like "hello" or "3.5", display a helpful error message instead of crashing.
try:
    user_input = input("Please enter an integer: ")
    user_integer = int(user_input)
    print(f"You entered the integer: {user_integer}")

except ValueError:
    print("Error: Please enter a valid integer.")


#2. Take two numbers and an operator. Handle:
# - Invalid number input
# - Division by zero
# - Invalid operators
try:
    num1 = float(input("Enter the first number:5"))
    num2 = float(input("Enter the second number:"))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator. Please use +, -, *, or /.")

    print(f"The result of {num1} {operator} {num2} is: {result}")
except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError as zde:
    print(f"Error: {zde}")


#3. Create a list of five items. Ask the user for an index and display the corresponding item. Handle invalid integer input and indexes outside the list.
try:
    lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    index_input = input("Enter an index (0-4) to retrieve an item from the list: ")
    index = int(index_input)
    item = lst[index]
    print(f"The item at index {index} is: {item}")
except ValueError:
    print("Error: Please enter a valid integer.")
except IndexError:
    print("Error: Index is out of bounds. Please enter an index between 0 and 4.")


#4. Create a dictionary of students and their marks. Ask for a student's name and display their marks. Handle a name that does not exist.
# Challenge: Handle unexpected input types too, without catching every possible exception indiscriminately.
try:
    students_marks = {
        'Husnaak' : 99,
        'Basit' : 95,
        'Sachin': 93,
        'Ali' : 88
    }
    name = input("Enter the student's name:")
    marks = students_marks[name]
    print(f"{name}'s marks are: {marks}")
except KeyError:
    print("Error: Student not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#5. Ask for a filename and attempt to open it for reading. If the file does not exist, show a suitable message
try:
    filename = input("Enter the filename to open: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#6. Write a function get_positive_number() that asks for a number and returns it only if it is positive.
# Requirements:
# - Handle non-numeric input.
# - Reject zero and negative numbers.
# - Keep asking until valid input is provided
def get_positive_number():
    while True:
        try:
            user_input = input("Please enter a positive number: ")
            number = float(user_input)
            if number <= 0:
                print("Error: The number must be positive. Please try again.")
            else:
                return number
        except ValueError:
            print("Error: Please enter a valid number.")
print(get_positive_number())

 
#7. Create a login system with a predefined username and password.
# Requirements:
# - Allow only three attempts.
# - Handle an empty username or password.
# - Handle unexpected errors where appropriate.
# - Display a lockout message after three failed attempts.
try:
    usrnme = "admin"
    pswrd = "password123"
    attempts = 0
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not username or not password:
            print("Error: Username and password cannot be empty.")
            continue

        if username == usrnme and password == pswrd:
            print("Login successful!")
            break
        else:
            attempts += 1
            print(f"Error: Invalid username or password. Attempts left: {3 - attempts}")
    else:
        print("Error: Too many failed attempts. Account locked.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#8. Ask for marks in five subjects.
# Requirements:
# - Accept only numeric marks.
# - Reject marks below 0 or above 100.
# - Do not accept invalid input as a valid mark.
# - Calculate total, percentage, and grade once all five marks are valid.

def get_marks():
    marks = []
    subjects = ['Math', 'Science', 'English', 'History', 'Art']
    
    for subject in subjects:
        while True:
            try:
                mark_input = input(f"Enter marks for {subject} (0-100): ")
                mark = float(mark_input)
                if mark < 0 or mark > 100:
                    print("Error: Marks must be between 0 and 100. Please try again.")
                else:
                    marks.append(mark)
                    break
            except ValueError:
                print("Error: Please enter a valid number.")
    
    total = sum(marks)
    percentage = total / len(marks)
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
get_marks()

