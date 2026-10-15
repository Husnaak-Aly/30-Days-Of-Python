x = input("Enter the number or word to check for Palindrome:")
reverse = ""
for i in reversed(x):
    reverse += i
if x == reverse:
    print("Palindrome!")
else:
    print("Not Palindrome!")
    
