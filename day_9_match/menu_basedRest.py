# Menu-Based Restaurant

# Display:

# 1. Burger
# 2. Pizza
# 3. Pasta
# 4. Sandwich

# Input choice and print item price.

# Example:

# Choice: 2
# Pizza costs Rs. 1200

print('''
    1. Burger
    2. Pizza
    3. Pasta
    4. Sandwich
          ''')

choice = input("Enter your choice:").strip(" ")

match choice:
    case char if not char.isdigit() or int(choice) > 4 :
        print("Invalid choice")
    case "1":
        print("Burger costs Rs.500")
    case "2":
        print("Pizza costs Rs. 1200")
    case "3":
        print("Pasta costs Rs. 700")
    case "4":
        print("Sandwich costs Rs. 600")

   