# Balance = 5000

# Ask user for withdrawal amount.

# If amount exceeds balance → "Insufficient funds"
# Otherwise → print remaining balance

balance = 5000
amount = int(input("Enter the amount you want to withdraw:"))

if amount % 500 != 0:
    print("You can only withdraw money in the multiples of 500")
else:
    if amount > balance:
        print("Insufficient funds!")
    else:
        print(f"Amount withdrawn successfully. Remaining amount is {balance - amount}")