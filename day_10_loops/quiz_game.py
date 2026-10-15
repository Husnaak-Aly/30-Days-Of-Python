# score = 0
# for i in range(5):
#     if i == 0:
#         first = input("What is the full name of Pakistan: (a) Islamic Republic of Pakistan  (b) Democratic Republic of Pakistan ").lower().strip()
#         match first:
#             case "a":
#                 print("Correct answer")
#                 score += 1
#             case "b":
#                 print("Wrong answer")
#                 if score == 0:
#                     continue
#                 else:
#                     score -=1
#             case _:
#                 print("Invalid option")
#     elif i == 1:
#         second = input("What is the national animal of Pakistan: (a) Ibex  (b) Markhor ").lower().strip()
#         match second:
#             case "a":
#                 print("Wrong answer")
#                 if score == 0:
#                     continue
#                 else:
#                     score -= 1
#             case "b":
#                 print("Correct answer")
#                 score +=1
#             case _:
#                 print("Invalid option")
#     elif i == 2:
#         third = input("Who is the PM of Pakistan: (a) Shahbaz Shareef  (b) Bilawal Bhutto ").lower().strip()
#         match third:
#             case "a":
#                 print("Correct answer")
#                 score += 1
#             case "b":
#                 print("Wrong answer")
#                 if score == 0:
#                     continue
#                 else:
#                     score -=1
#             case _:
#                 print("Invalid option")
#     elif i == 3:
#         fourth = input("Largest city of Pakistan: (a) Karachi  (b) Larkana ").lower().strip()
#         match fourth:
#             case "a":
#                 print("Correct answer")
#                 score += 1
#             case "b":
#                 print("Wrong answer")
#                 if score == 0:
#                     continue
#                 else:
#                     score -=1
#             case _:
#                 print("Invalid option")
#     elif i == 4:
#         fifth = input("What is the largest river of Pakistan: (a) Ravi river  (b) Indus River ").lower().strip()
#         match fifth:
#             case "a":
#                 print("Wrong answer")
#                 if score == 0:
#                     continue
#                 else:
#                     score -= 1
#             case "b":
#                 print("Correct answer")
#                 score += 1
#             case _:
#                 print("Invalid option")
# print(f"Final score is {score}")    

    


# Pro tip -------> Separate the logic from data


quiz_data = [
    {
        "q": "What is the full name of Pakistan:\n(a) Islamic Republic of Pakistan\n(b) Democratic Republic of Pakistan\n",
        "ans": "a"
    },
    {
        "q": "What is the national animal of Pakistan:\n(a) Ibex\n(b) Markhor\n",
        "ans": "b"
    },
    {
        "q": "Who is the PM of Pakistan:\n(a) Shahbaz Sharif\n(b) Bilawal Bhutto\n",
        "ans": "a"
    },
    {
        "q": "Largest city of Pakistan:\n(a) Karachi\n(b) Larkana\n",
        "ans": "a"
    },
    {
        "q": "What is the largest river of Pakistan:\n(a) Ravi river\n(b) Indus River\n",
        "ans": "b"
    }
]

score = 0
for item in quiz_data:
    choice = input(item['q']).lower().strip()
    if choice == item["ans"]:
        print("Correct answer")
        score += 1
    elif choice in ['a', 'b']:
        print("Wrong answer")
    else:
        print("Invalid option!")
print(f"Your score is {score} out of {len(quiz_data)}")