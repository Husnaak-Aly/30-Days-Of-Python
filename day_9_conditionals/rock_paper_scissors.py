# Take inputs from two players and determine the winner using conditionals only.
player1 = input("Player One: Enter your weapon:").lower().strip(" ")
player2 = input("Player Two: Enter your weapon:").lower().strip(" ")
weapons = {"rock", "paper", "scissors"}
opted = {player1, player2}

if opted.issubset(weapons):
    if player1 == "rock":
        if player2 == "rock":
            print("Try again!")
        elif player2 == "paper":
            print("Player two won!")
        else:
            print("Player one won!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player one won")
        elif player2 == "paper":
            print("Try again!")
        else:
            print("Player two won!")
    elif player1 == "scissors":
        if player2 == "rock":
            print("Player two won!")
        elif player2 == "paper":
            print("Player one won!")
        else:
            print("Try again")
else:
    print("Wrong choice of weapon. Please choose from: (rock, paper, scissors)")

# pro tip: We can check first if player 1 = player 2 to make it much cleaner
# write updated code below
