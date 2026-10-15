# # Input a single character.

# # Print:

# # Vowel
# # Consonant
# # Digit
# # Special Character

# # Use match where possible.

charInput = input("Enter any single character:").lower().strip(" ")

if len(charInput) != 1:
    print("Error: Please enter exactly one character.")
else:
    match charInput:
        case char if char in "aeiou":
            print("Vowel")
        case char if char.isalpha():
            print("Consonant")
        case char if char.isdigit():
            print("Digit")
        case _:
            print("Special character")
        





