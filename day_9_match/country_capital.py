# Input country:

# Pakistan
# China
# Japan
# Turkey

# Print capital city.

concap = {"pakistan" : "Islamabad", "china" : "Beijing", "japan" : "Tokyo", "turkey" : "Ankara"}
print("""Choose the Country:
      1. Pakistan
      2. China
      3. Japan
      4. Turkey""")
country = input("=>").lower().strip(" ")
match country:
    case "pakistan":
        print("Capital of Pakistan is", concap[country])
    case "china":
        print("Capital of China is", concap[country])
    case "japan":
        print("Capital of Japan is", concap[country])
    case "turkey":
        print("Capital of Turkey is", concap[country])
    case _:
        print("Invalid choice. This country is not in the list")