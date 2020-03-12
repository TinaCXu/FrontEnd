choice = input("Do you want to start a new game?(Y/N)")
while (choice == "Y"):
    player1 = input("Player1: Please enter your choice: ")
    player2 = input("Player2: Please enter your choice: ")
    if player1 == "rock":
        if (player2 == "rock"):
            print ("Draw")
        if (player2 == "sissors"):
            print ("Player1 win")
        if (player2 == "paper"):
            print ("Player2 win")
    if (player1 == "sissors"):
        if (player2 == "rock"):
            print ("Player2 win")
        if (player2 == "sissors"):
            print ("Draw")
        if (player2 == "paper"):
            print ("Player1 win")
    if (player1 == "paper"):
        if (player2 == "rock"):
            print ("Player1 win")
        if (player2 == "sissors"):
            print ("Player2 win")
        if (player2 == "paper"):
            print ("Draw")
    choice = input("Do you want to start a new game?(Y/N)")
if (choice == "N"):
    print ("Bye")
