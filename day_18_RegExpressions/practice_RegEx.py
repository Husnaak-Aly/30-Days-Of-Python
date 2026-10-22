import re
#1. Find All Digits
text = "My roll number is 23SW048 and I am in semester 6."
ptrn = r'\d'
match = re.findall(ptrn, text)
print(match)

#2. Find All Words Starting with a Capital Letter
text = "Ali studies Software Engineering at Mehran University."
ptrn = r'\b[A-Z]\w*\b' 
matches = re.findall(ptrn,text)
print(matches)


#3.Count Vowels Using Regex (regardless of capital or small letter)
text = "Regular Expressions Are Interesting"
ptrn = r'[aeiou]'
matches = re.findall(ptrn, text, re.I)
print("Total number of vowels present:",len(matches))


#4. Find All Words of a Specific Length. Extract all words containing exactly five letters.
text = "Python makes coding easier for many people."
ptrn = r'\b\w{5}\b'
matches = re.findall(ptrn, text)
print(matches)

#5. Find Repeated Characters. Detect consecutive repeated characters in a string.
text = "hello bookkeeper committee"
ptrn = r'(.)\1+'
matches = re.findall(ptrn, text)
print(matches)


#6.Find All Occurrences of a Word. Find every occurrence of "python" regardless of capitalization.
text = "Python is great. I use PYTHON, and python is easy."
matches = re.findall('python', text, re.I)
print(matches)


#7. Validate a username
# Length must be 5–15 characters.
# Only letters, digits, and underscores are allowed.
# It must start with a letter.
def validate_username(username):
    validity = r'[a-zA-Z]\w{4,14}'
    if re.fullmatch(validity,username):
        return "valid"
    return "invalid"
print(validate_username("husnaak_123"))


#8. Validate a Pakistani Phone Number
# Write a function that validates phone numbers in these formats:
# 03001234567
# +923001234567
# 92300123456
def validate_number(num):
    valid_num = r'[09+]\d{10,12}'
    if re.fullmatch(valid_num,num):
        return "valid"
    return "invalid"
print(validate_number("03133356464"))


#9. Validate an Email Address
# Create validate_email(email).
# For this exercise, use a practical simplified rule:
# - One @ symbol.
# - A non-empty username.
# - A domain name.
# - A dot followed by a domain suffix.
def validate_email(email):
    valid_email = r'[a-zA-Z]\w*@\w+\.com'
    if re.fullmatch(valid_email, email):
        return "valid email"
    return "invalid email"
print(validate_email("husnaak@gmail.com"))


#10. Extract Email Addresses
text = """Contact ali@gmail.com, sara@yahoo.com,and support@example.org for assistance."""
# Extract all email addresses into a list.
email_ptrn = r'[a-zA-Z]\w*@\w+\.com'
all_emails = re.findall(email_ptrn,text, re.I)
print(all_emails)
