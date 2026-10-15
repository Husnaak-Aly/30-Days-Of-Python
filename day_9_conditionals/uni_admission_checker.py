# Ask for:

# Matric percentage
# Intermediate percentage

# Rules:

# Matric ≥ 60 and Intermediate ≥ 60 → Eligible
# Otherwise → Not Eligible

# Challenge: Add merit categories:

# 85+ → High Merit
# 70–84 → Medium Merit
# 60–69 → Low Merit
# Below 60 → Not Eligible

m_p = float(input("Enter Matric percentage:"))
i_p = float(input("Enter Intermediate percentage:"))

if m_p >=60 and i_p >= 60:
    if m_p >= 85:
        print("Eligible. High merit!")
    elif m_p >= 70 and m_p < 85:
        print("Eligible. Medium merit!")
    else:
        print("Eligible. Low merit!")
else:
    print("Not Eligible!")
