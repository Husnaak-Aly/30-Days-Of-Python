secret = 7
for i in range(5):
    inp = int(input(f"Attempt {i+1}. Guess the number:"))
    if inp == secret:
        print("Correct")
        break
    elif inp < secret:
        print("Too Low")
    else:
        print("Too High")
