# Password Attempts
# Correct password:
# python123
# Give the user 3 attempts.
# Print:
# Access Granted
# Account Locked

attempts = 0

while attempts < 3:
    pw = input(f"Attempt {attempts+1}. Enter password:")
    if pw == 'python123':
        print("Access Granted!")
        break
    attempts += 1
else:
    print("Access locked")
