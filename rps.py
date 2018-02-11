from random import randint

# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[randint(0, 2)]

# set player to False
player = False

while player == False:
    # set player to True
    player = str(raw_input("(R)ock, (P)aper, (S)cissor?"))
    if player[0].upper() == computer[0]:
        print("Tie!")
    elif player.upper() == "R":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player.upper() == "P":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player.upper() == "S":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. R, P, S?")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]