# Ask for:

# Weight (kg)
# Height (m)

# Calculate BMI:

# BMI = weight / (height ** 2)

# Print:

# Underweight (<18.5)
# Normal (18.5–24.9)
# Overweight (25–29.9)
# Obese (30+)


weight = int(input("Enter your weight (kg):"))
height = float(input("Enter your height (ft):"))
height_m = height * .3048
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")