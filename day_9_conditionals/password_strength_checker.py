
# Ask for a password.

# Print:

# "Strong" if length is 8 or more.
# "Weak" otherwise.

# Bonus: Also check if it contains a number.
pw = input("Enter the password:")
x = len(pw)

if " " in pw:
    print("Password can not contain spaces")
elif x >= 8 and any(char.isdigit() for char in pw) and any(char.isupper() for char in pw):
    print("Strong password")
else:
    print("Weak password")

#better version
if " " in pw:
    print("Password can not contain spaces!")
else:
    if x < 8:
        print("Weak Password. It must be at least 8 characters long.")
    elif not any(char.isdigit() for char in pw):
        print("Weak Password. It should contain at least 1 digit.")
    elif not pw[0].isupper():
        print("Weak password. First character must be capital.")
    else:
        print("Strong password.")
