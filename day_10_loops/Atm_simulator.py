# Add loops so the menu keeps showing until the user chooses Exit.
# Use:
# Balance inquiry
# Deposit
# Withdraw
# Exit
Balance = 5000
while True:
    print("""
    ========ATM Service=======
    "1. Balance Inquiry" 
    "2. Deposit" 
    "3. Withdraw" 
    "4.Exit""")

    x = int(input("Enter choice:"))
    match x:
        case 1:
            print(f"Your current balance is Rs.{Balance}.")
        case 2:
            new_balance = int(input("Enter the amount you want to deposit:"))
            Balance += new_balance
            print(f"Your new balance is Rs.{Balance}.") 
        case 3:
            amount = int(input("Enter the amount you want to withdraw:"))
            if amount > Balance:
                print(f"You have Insufficient funds. You can only withdraw up to Rs.{Balance}.")
            elif amount > 0 and amount <= Balance:
                Balance -= amount
                print(f"You have successfully withdrawn Rs.{amount}. Remaining balance Rs.{Balance}")
            else:
                print("Invalid Request")
        case 4:
            print("Thank You for using ATM service.")
            break
        case _:
            print("Invalid Choice")

