# Input a color:

# "red" → Stop
# "yellow" → Slow down
# "green" → Go

# Anything else → Invalid signal.

color = input("Enter the color:").lower().strip(" ")

match color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Slow down!")
    case "green":
        print("Go!")
    case _:
        print("Invalid signal!")